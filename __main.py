import scrapy


class MySpider(scrapy.Spider):
    name = 'coingeko'
    start_urls = 'https://www.coingecko.com/en/coins/bitcoin'

    def parse(self, response, **kwargs):
        print()

