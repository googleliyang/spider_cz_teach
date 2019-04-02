# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class MyspiderPipeline(object):

    def __init__(self):
        self.file = open('itcast.json', 'w')

    # 该方法必须被重写
    def process_item(self, item, spider):
        # print("python37:", item)

        str_data = json.dumps(item, ensure_ascii=False) + ',\n'
        self.file.write(str_data)

        # 每一个process_item方法在使用完数据之后必须返回数据
        return item

    def __del__(self):
        self.file.close()
