''' using this to store logic and code for the basic biodata and information about the 
    charities
'''

import scrapy
from scrapy_playwright.page import PageMethod

class CharityProfileSpider(scrapy.Spider):
    name = "organisation_profile" # unique identifier for the Spider
    start_urls = ["https://www.charities.gov.sg/Pages/AdvanceSearch.aspx"]

    # function to have playwright click on search button to load charity profiles
    def start_requests(self):
        yield scrapy.Request(
            url=self.start_urls[0],
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    PageMethod("click", "button#btnSearchClk"), # referenced search button by ID
                ],
            },
            callback=self.parse,
            )

    # function to process page content after button click
    def parse(self, response):
        # Extract total count of charity profiles in portal
        charity_profile_count = response.css("span.charities filter-records::text").get()
        print("Total number of charity records are", charity_profile_count)
        # Test: extract current page charity links first
        # Extract charity links
        charity_links = response.css('a[rel="noopener noreferrer"]::attr(href)').getall()

        for link in charity_links:
            yield scrapy.Request(
                url=response.urljoin(link),
                meta={
                    "playwright": True,
                    "playwright_page_methods": [
                        # waiting for org profile tab to be active
                        PageMethod("wait_for_selector", 'li[data-target="#tabProfile"][data-state="active"]', timeout=15000),
                        # waiting for tab content to load 
                        PageMethod("wait_for_selector", 'div#tabProfile', timeout=15000),
                        PageMethod("wait_for_load_state", "networkidle"),
                    ],
                },
                callback=self.parse_charity_profile
            )
            
    # function to extract relevant org profile data from charity page
    # issue: need Playwright to help wait for the page to load the data    
    def parse_charity_profile(self, response):
        yield {
            "uen": response.css('//*[@id="tabProfile"]/div[1]/div[1]/p::text').get(),
            "contact_person": response.css('//*[@id="tabProfile"]/div[1]/div[2]/p::text').get(),
            "registration_date": response.css('//*[@id="tabProfile"]/div[2]/div[1]/p::text').get(),
            "charity_setup": response.css('//*[@id="tabProfile"]/div[2]/div[2]/p::text').get(),
            "office_no": response.css('//*[@id="tabProfile"]/div[3]/div[1]/p::text').get(),
            "status_of_charity": response.css('//*[@id="tabProfile"]/div[3]/div[2]/p::text').get(),
            "fax_no": response.css('//*[@id="tabProfile"]/div[4]/div[1]/p::text').get(),
            "ipc_status": response.css('//*[@id="tabProfile"]/div[4]/div[2]/p::text').get(),
            "email_address": response.css('//*[@id="tabProfile"]/div[5]/div[1]/p/a::attr(href)').get(),
            "sector_administrator": response.css('//*[@id="tabProfile"]/div[6]/div[2]/p::text').get(),
            "website": response.css('//*[@id="tabProfile"]/div[7]/div[1]/p/a::attr(href)').get(),
            "last_profile_update": response.css('//*[@id="tabProfile"]/div[7]/div[2]/p::text').get(), # very important field

            # multi-line text extraction
            "objectives": response.css('//*[@id="tabProfile"]/p[1]::text').get(),
            "vision_and_mission": response.css('//*[@id="tabProfile"]/p[2]::text').get(),
            "organisation_activities": response.css('//*[@id="tabProfile"]/ul/li::text').getall(), # data stored in seperate ul li elements
            
            # extracting table data
            "patrons": self.extract_table_data(response, '#tblPatrons'),
            "governing_board_members": self.extract_table_data(response, '#tblGoverningBoardMembers'),
            "key_officers": self.extract_table_data(response, '#tblKeyOfficers')
        }


        # issue: dealing with tables with pagination for patrons, board members & key officers
        def extract_table_data(self, response, table_id):
            table_data = [] # storing extract table data in this list
            rows = response.css('//*[@id="table_id"]/tbody/tr')
            # both key officers and governing board members table have a similar schema - extract Full Name & Designation
            # patrons just need to extract their full names
            for row in rows:
                if row.css('td.dataTables_empty'):
                    continue
                else:

            pass

        # likely we need to check if pagination is present
        # if pagination is present in the table, we would need to fetch the links - do note the href uses # which is likely JS
        # extract table information - I would like to extract table by table to avoid clashing info
        # skip table if no records found
