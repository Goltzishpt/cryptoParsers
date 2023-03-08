# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2


class PostgresPipeline:

    # def __init__(self):
    #     self.create_connection()
    #
    # def create_connection(self):
    #     hostname = 'localhost'
    #     username = 'postgres'
    #     password = '123456'
    #     database = 'quotes'
    #
    #     self.connection = psycopg2.connect(
    #         host=hostname,
    #         user=username,
    #         password=password,
    #         dbname=database
    #     )
    #
    #     self.cur = self.connection.cursor()
    #

    def process_item(self, item, spider):
        return

