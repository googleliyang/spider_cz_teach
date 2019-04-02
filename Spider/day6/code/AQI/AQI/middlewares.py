# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from scrapy.http import HtmlResponse
import time


class SeleniumMiddleware(object):

    def process_request(self, request, spider):

        url = request.url

        if 'daydata' in url:
            driver = webdriver.Chrome()

            driver.get(url)
            time.sleep(3)

            data = driver.page_source

            driver.close()

            # 构建响应对象
            res = HtmlResponse(
                url=url,
                body=data,
                request=request,
                encoding='utf-8'
            )
            # 中间件中返回数据必须使用return
            return res