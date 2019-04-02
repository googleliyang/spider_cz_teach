# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#arobot']

    def parse(self, response):
        # with open("temp1.html","wb")as f:
        #     f.write(response.body)
        # with open("temp2.html","w")as f:
        #     f.write(response.text)    

        # 获取所有教师节点
        el_list = response.xpath('//div[@class="li_txt"]')
        # print(len(el_list))

        for el in el_list:
            temp = {}

            temp['name'] = el.xpath('./h34/text()').extract_first()
            temp['title'] = el.xpath('./h4/text()').extract_first()
            temp['desc'] = el.xpath('./p/text()').extract_first()

            # temp['name'] = el.xpath('dsfds')[0].extract() if len(el.xpath('dsfds')) > 0 else None

            print(temp)
