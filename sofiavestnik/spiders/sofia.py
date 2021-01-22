import scrapy


class SofiaSpider(scrapy.Spider):
    name = 'sofia'
    allowed_domains = ['sofiavestnik.com']
    start_urls = ['http://sofiavestnik.com/']

    def parse(self, response):
        pass
