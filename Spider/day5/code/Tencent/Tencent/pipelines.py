# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from pymongo import MongoClient
from Tencent.settings import MONGO_HOST,MONGO_PORT


class TencentPipeline(object):

    def open_spider(self, spider):
        if spider.name == "tencent":
            self.file = open('tencent.json', 'w')

    def process_item(self, item, spider):
        if spider.name == "tencent":
            str_data = json.dumps(dict(item)) + ',\n'

            self.file.write(str_data)

        return item

    def close_spider(self, spider):
        if spider.name == "tencent":
            self.file.close()


class TencentProPipeline(object):

    def open_spider(self, spider):
        if spider.name == "tencentpro":
            self.file = open('tencentpro.json', 'w')

    def process_item(self, item, spider):
        if spider.name == "tencentpro":
            str_data = json.dumps(dict(item)) + ',\n'

            self.file.write(str_data)

        return item

    def close_spider(self, spider):
        if spider.name == "tencentpro":
            self.file.close()


class MongoPipeline(object):

    def open_spider(self, spider):
        self.client = MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.client['python37']
        self.col = self.db['tencent']

    def process_item(self, item, spider):

        dict_data = dict(item)

        self.col.insert(dict_data)

        return item

    def close_spider(self, spider):
        self.client.close()