import re
import scrapy
from ..parsers.CoinGecko.parserCoinGecko import CryptoCurrencyCoinGeckoParse


class MySpider(scrapy.Spider):
    name = 'coingecko'
    custom_settings = {
        'DOWNLOAD_DELAY': 1,
        'LOG_LEVEL': 'INFO',
    }
    headers = {
        'host': 'www.coingecko.com'
    }
    url = 'https://www.coingecko.com/en/all-cryptocurrencies/show_more_coins?page={page}&per_page=300&'
    user_agent = 'Scrapy/1.3.0 (+http://scrapy.org)'

    def start_requests(self):
        yield scrapy.Request(url=self.url.format(page=1), callback=self.parse)

    def parse(self, response, **kwargs):
        xpath = '//descendant::a/@href'
        hrefs = response.xpath(xpath).getall()
        for href in hrefs:
            yield scrapy.Request(url=response.urljoin(href), callback=self.get_data)
        if len(hrefs) == 300:
            yield scrapy.Request(
                url=self.url.format(page=int(re.findall(r'\?page=(\d+)', response.url)[0]) + 1),
                callback=self.parse
            )

    def get_data(self, response):
        item = CryptoCurrencyCoinGeckoParse(response=response)
        print(item.get_item())
        yield item.get_item()
