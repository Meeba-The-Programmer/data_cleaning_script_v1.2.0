''' using this to store logic and code for the basic biodata and information about the 
    charities
'''

import scrapy
from playwright.async_api import async_playwright

class CharityProfileSpider(scrapy.Sider):
    name = "organisation_profile" # unique identifier for the Spider
    start_urls = ["data:,"]

    async def parse(self):
        urls = ["https://www.charities.gov.sg/Pages/AdvanceSearch.aspx"]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)