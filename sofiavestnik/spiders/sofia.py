import scrapy
from datetime import datetime
from sofiavestnik.items import Article
from itemloaders.processors import TakeFirst
from scrapy.loader import ItemLoader


class SofiaSpider(scrapy.Spider):
    name = 'sofia'
    allowed_domains = ['sofiavestnik.com']
    start_urls = ['http://sofiavestnik.com/']

    def parse(self, response):
        pass
