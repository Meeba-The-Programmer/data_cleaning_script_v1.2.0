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
        pass