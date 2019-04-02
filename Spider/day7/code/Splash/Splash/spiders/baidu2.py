# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


class Baidu2Spider(scrapy.Spider):
    name = 'baidu2'
    allowed_domains = ['baidu.com']
    start_urls = ['https://www.baidu.com/s?wd=python']

    def start_requests(self):
        url = self.start_urls[0]

        yield SplashRequest(
            url=url,
            callback=self.parse,
            args={'wait': 10},
            endpoint='render.html'
        )

    def parse(self, response):
        with open("baidu_with_splash.html","wb")as f:
            f.write(response.body)
