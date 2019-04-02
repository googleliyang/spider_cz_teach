# -*- coding: utf-8 -*-
import scrapy


class Baidu1Spider(scrapy.Spider):
    name = 'baidu1'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/s?wd=python']

    def parse(self, response):
        with open('baidu_without_splash.html','wb')as f:
            f.write(response.body)
