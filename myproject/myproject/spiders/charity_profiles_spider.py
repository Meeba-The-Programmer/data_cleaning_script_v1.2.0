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
        for charity in charity_links:
            yield response.follow(charity, self.parse_charity_profiles) 
            
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
            "objectives": response.css('//*[@id="tabProfile"]/p[1]::text').get(),
            "vision_and_mission": response.css('//*[@id="tabProfile"]/p[2]::text').get(),
            "organisation_activities": response.css('//*[@id="tabProfile"]/ul/li::text').getall(), # issue: data stored in seperate ul li elements
        }

        # issue: dealing with tables with pagination for patrons, board members & key officers