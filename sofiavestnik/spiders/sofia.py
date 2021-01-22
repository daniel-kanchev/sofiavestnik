import scrapy
from datetime import datetime
from sofiavestnik.items import Article
from itemloaders.processors import TakeFirst
from scrapy.loader import ItemLoader
import pprint


class SofiaSpider(scrapy.Spider):
    name = 'sofia'
    allowed_domains = ['sofiavestnik.com']
    start_urls = ['http://sofiavestnik.com/']

    def parse(self, response):
        articles = []
        pp = pprint.PrettyPrinter(indent=4)
        all_text = response.xpath("//table[@class='contentpaneopen']//text()").getall()
        all_text = [text.strip() for text in all_text if text.strip()]
        indexes_to_pop = []
        for i, text in enumerate(all_text):
            if text.isnumeric():
                all_text[i] += " " + all_text[i + 1]
                indexes_to_pop.append(i + 1)
        for index in indexes_to_pop:
            all_text.pop(index)

        article = {}
        for i, text in enumerate(all_text):
            if text.endswith(" г.") and text[:2].isnumeric():
                if 'content' in article.keys():
                    article['content'].pop(-1)
                    articles.append(article)
                    article = {}
                article['date'] = text
                article['title'] = all_text[i - 1]

            else:
                if 'date' in article.keys():
                    if 'content' not in article.keys():
                        article['content'] = []
                    article['content'].append(text)

        for article in articles:
            article['content'] = "\n".join(article['content'])
            item = ItemLoader(Article(), TakeFirst)
            item.default_output_processor = TakeFirst()
            item.add_value('title', article['title'])
            item.add_value('date', format_date(article['date']))
            item.add_value('content', article['content'])

            yield item.load_item()


def format_date(date):
    date_dict = {
        "януари": "January",
        "февруари": "February",
        "март": "March",
        "април": "April",
        "май": "May",
        "юни": "June",
        "юли": "July",
        "август": "August",
        "септември": "September",
        "октомври": "October",
        "ноември": "November",
        "декември": "December",
    }
    date = date.split()
    date.pop(-1)
    for key in date_dict.keys():
        if date[1] == key:
            date[1] = date_dict[key]

    date = " ".join(date)
    date_time_obj = datetime.strptime(date, '%d %B %Y')
    date = date_time_obj.strftime("%Y/%m/%d")
    return date
