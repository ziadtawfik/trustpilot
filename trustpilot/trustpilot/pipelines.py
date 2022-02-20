# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

from scrapy import Item

class TrustpilotPipeline:
    def __init__(self):
        self.con = sqlite3.connect('trustpilot.db')
        self.cur = self.con.cursor()

    def create_table(self ,table_name):
        self.cur.execute(f"""CREATE TABLE IF NOT EXISTS {table_name}(
        name TEXT,
        score TEXT,
        reviews_number TEXT,
        categories TEXT,
        adresses TEXT)
        """)


    def process_item(self, item, spider):
        self.create_table(spider.table)
        self.cur.execute(f"""INSERT OR IGNORE INTO {spider.table} VALUES(?,?,?,?,?)""",
        (
            item['name'][0],
            item['score'][0],
            item['reviews_number'][0],
            item['categories'][0],
            item['adresses'][0]
            ))
        self.con.commit()
        return item