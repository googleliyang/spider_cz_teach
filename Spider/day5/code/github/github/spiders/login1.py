# -*- coding: utf-8 -*-
import scrapy


class Login1Spider(scrapy.Spider):
    name = 'login1'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/exile-morganna']

    def start_requests(self):
        url = self.start_urls[0]

        temp = '_ga=GA1.2.1190047373.1543731773; _octo=GH1.1.1199554731.1543731773; user_session=IsN0sqpV56zDyNOGBoUWHPRtiIe25zQ0y2cUCmBw0ubT7Zta; __Host-user_session_same_site=IsN0sqpV56zDyNOGBoUWHPRtiIe25zQ0y2cUCmBw0ubT7Zta; logged_in=yes; dotcom_user=exile-morganna; has_recent_activity=1; _gat=1; tz=Asia%2FShanghai; _gh_sess=RkttQVcya0dQT1VNNGF1d0Z6eFN2RHQ3ZEVXYXQ1QVdmeExFUFlxSSt1cFgwTEpCZHI3ZUQxVWFCTkRKM1BMR1lOWmpTZUI2Nk1TOUJ1a2dZeUZpK2ZYdElsS3ZER3Z4YUE1SzNBWFcwN1BjeTNpNURQK29KTGtyVFQ2eC9jVXgrclkwaFovdjQwbHRVSlh3Tm9zWlhBPT0tLTdDNVYxcHQwZEVubzcwQU1nU3VaU1E9PQ%3D%3D--aa073f9f24d82d7415b2c0d8c9d5a0cefe4a2f57'
        cookies = {data.split('=')[0]: data.split('=')[-1] for data in temp.split('; ')}

        yield scrapy.Request(
            url=url,
            dont_filter=True,
            cookies=cookies
        )

    def parse(self, response):
        with open('login_with_cookies.html','wb')as f:
            f.write(response.body)
