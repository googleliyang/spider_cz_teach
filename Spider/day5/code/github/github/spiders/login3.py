# -*- coding: utf-8 -*-
import scrapy


class Login3Spider(scrapy.Spider):
    name = 'login3'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        # 从响应中提取数据，构建formdata
        #
        # utf8 = response.xpath('//*[@name="utf8"]/@value').extract_first()
        # authenticity_token = response.xpath('//*[@name="authenticity_token"]/@value').extract_first()
        # commit = response.xpath('//*[@name="commit"]/@value').extract_first()
        # webauthn_support = response.xpath('//*[@name="webauthn-support"]/@value').extract_first()

        formdata = {
            "login": "exile-morganna",
            "password": "1QAZ2wSX3edC4rfv",
        }

        yield scrapy.FormRequest.from_response(response,formdata=formdata,callback=self.after_login)

    def after_login(self, response):
        yield scrapy.Request('https://github.com/exile-morganna', callback=self.check_login)

    def check_login(self, response):
        with open('login_with_fromresponse.html', 'wb')as f:
            f.write(response.body)
