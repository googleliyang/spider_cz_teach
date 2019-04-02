# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from pymongo import MongoClient

# class TencentPipeline(object):
#
#     def __init__(self):
#         self.file = open("tencent.json", "w")
#
#     # process_item方法负责定义对数据的处理
#     def process_item(self, item, spider):
#
#         # 将item对象转换成Python字典
#         item = dict(item)
#
#         str_data = json.dumps(item,ensure_ascii=False) + ',\n'
#
#         self.file.write(str_data)
#
#         # 管道处理完item之后必须将item对象返回给引擎
#         return item
#
#     def __del__(self):
#         self.file.close()
#
#
# class TencentProPipeline(object):
#
#     def __init__(self):
#         self.file = open("tencentpro.json", "w")
#
#     # process_item方法负责定义对数据的处理
#     def process_item(self, item, spider):
#
#         # 将item对象转换成Python字典
#         item = dict(item)
#
#         str_data = json.dumps(item,ensure_ascii=False) + ',\n'
#
#         self.file.write(str_data)
#
#         # 管道处理完item之后必须将item对象返回给引擎
#         return item
#
#     def __del__(self):
#         self.file.close()


class TencentPipeline(object):

    def open_spider(self, spider):
        if spider.name == "tencent":
            self.file = open("tencent.json", "w")

    # process_item方法负责定义对数据的处理
    def process_item(self, item, spider):

        if spider.name == "tencent":
            # 将item对象转换成Python字典
            item = dict(item)

            str_data = json.dumps(item,ensure_ascii=False) + ',\n'

            self.file.write(str_data)

        # 管道处理完item之后必须将item对象返回给引擎
        return item

    def close_spider(self, spider):
        if spider.name == "tencent":
            self.file.close()


class TencentProPipeline(object):

    def open_spider(self, spider):
        # spider中记录了爬虫名，可以根据爬虫名决定是否使用管道
        if spider.name == "tencentpro":
            self.file = open("tencentpro.json", "w")

    # process_item方法负责定义对数据的处理
    def process_item(self, item, spider):

        if spider.name == "tencentpro":
            # 将item对象转换成Python字典
            item = dict(item)

            str_data = json.dumps(item,ensure_ascii=False) + ',\n'

            self.file.write(str_data)

        # 管道处理完item之后必须将item对象返回给引擎
        return item

    def close_spider(self, spider):
        if spider.name == "tencentpro":
            self.file.close()


class MongoPipeline(object):

    def open_spider(self, spider):
        # spider中记录了爬虫名，可以根据爬虫名决定是否使用管道
        self.cli = MongoClient("127.0.0.1",27017)
        self.col = self.cli.python19.qq

    # process_item方法负责定义对数据的处理
    def process_item(self, item, spider):

        # 将item对象转换成Python字典
        item = dict(item)

        self.col.insert(item)

        # 管道处理完item之后必须将item对象返回给引擎
        return item

    def close_spider(self, spider):

        self.cli.close()
