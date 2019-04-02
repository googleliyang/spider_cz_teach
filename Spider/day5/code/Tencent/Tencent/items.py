# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link = scrapy.Field()
    type = scrapy.Field()
    num = scrapy.Field()
    address = scrapy.Field()
    date = scrapy.Field()
    pass

class TencentProItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    link = scrapy.Field()
    type = scrapy.Field()
    num = scrapy.Field()
    address = scrapy.Field()
    date = scrapy.Field()

    duty = scrapy.Field()
    require = scrapy.Field()
    pass

    # 建模之后，需要采集的数据的条目清晰
    # 模板类的实例具有key的检查功能，同时使用方法同dict

# if __name__ == '__main__':
#     # mydata = {}
#     # mydata['name'] = '王老师'
#     # mydata['title'] = '高级讲师'
#     # mydata['desc'] = '高级讲师dgkdsflksdjf'
#     # mydata['neme'] = "djkhdksfhjdks"
#     # print(mydata)
#
#     item = TencentItem()
#     item['name'] = "网"
#     item['link'] = "http://www.baidu.com"
#     item['neme'] = "dgdsfkhjdk"
#     print(item)