import scrapy
import json
import pprint
from crawler.parsers.CoinMarketCap.parserCoinMarketCap import CryptoCurrencyCoinMarketCapParse


class CoinMarketCapAllSpider(scrapy.Spider):
    name = 'coinmarketcap'
    custom_settings = {
        'DOWNLOAD_DELAY': 1,
        'LOG_LEVEL': 'INFO'
    }
    headers = {
        'host': 'https://coinmarketcap.com/'
    }
    url = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=10000&sortBy=market_cap&' \
          'sortType=desc&convert=USD,BTC,ETH&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,' \
          'num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,' \
          'self_reported_circulating_supply,self_reported_market_cap'

    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(
            url=self.url, callback=self.parse
        )

    def parse(self, response, **kwargs):
        items = json.loads(response.text)['data']['cryptoCurrencyList']
        for item in items[:3]:
            yield scrapy.Request(
                url=f'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/detail?id={item["id"]}',
                callback=self.get_data,
            )

    def get_data(self, response):
        item = CryptoCurrencyCoinMarketCapParse(response=response)
        pprint.pprint(item.get_item())
        yield item.get_item()



# https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=10000&sortBy=market_cap&sortType=desc&convert=USD,BTC,ETH&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,max_supply,circulating_supply,total_supply,volume_7d,volume_30d,self_reported_circulating_supply,self_reported_market_cap
# https://api.coinmarketcap.com/data-api/v3/cryptocurrency/detail?id=2011
