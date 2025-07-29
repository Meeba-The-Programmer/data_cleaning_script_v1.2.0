BOT_NAME = "myproject"

SPIDER_MODULES = ["myproject.spiders"]
NEWSPIDER_MODULE = "myproject.spiders"

ROBOTSTXT_OBEY = True

DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
PLAYWRIGHT_BROWSER_TYPE = "chromium"
