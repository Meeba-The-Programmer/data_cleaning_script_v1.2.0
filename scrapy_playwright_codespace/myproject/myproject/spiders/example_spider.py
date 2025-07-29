import scrapy
from scrapy_playwright.page import PageCoroutine

class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ["https://quotes.toscrape.com/js"]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url,
                meta={
                    "playwright": True,
                    "playwright_page_coroutines": [
                        PageCoroutine("wait_for_selector", "div.quote")
                    ]
                }
            )

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get()
            }
