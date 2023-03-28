# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2
from settings import DB_CONFIG


class PostgresPipeline:

    def __init__(self, db_config):
        self.db_config = db_config

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            db_config=crawler.settings.getdict('DB_CONFIG')
        )

    def open_spider(self, spider):
        self.connection = psycopg2.connect(**self.db_config)
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cursor.execute(
                """
                INSERT INTO cryptocurrency
                (id, name, rank, symbol, url, image, explorers, wallets, community, tags, market_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (name, symbol, market_id) DO UPDATE SET 
                name = excluded.name,
                rank = excluded.rank,
                symbol = excluded.symbol,
                url = excluded.url,
                contracts = excluded.contracts,
                image = excluded.image,
                explorers = excluded.explorers,
                wallets = excluded.wallets,
                community = excluded.community,
                tags = excluded.tags,
                market_id = excluded.market_id;
                """, (item['id'], item['name'], item['rank'], item['symbol'], item['url'], item['contracts'],
                item['image'], item['explorers'], item['wallets'], item['community'], item['tags']))
            self.connection.commit()
        except psycopg2.Error as e:
            self.connection.rollback()
            spider.log(f'Error: {e}')

