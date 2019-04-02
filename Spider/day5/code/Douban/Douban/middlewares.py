# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from Douban.settings import USER_AGENT_LIST,PROXY_LIST
import random
import base64

class RandomUserAgent(object):

    def process_request(self, request, spider):

        ua = random.choice(USER_AGENT_LIST)

        request.headers['User-Agent'] = ua


class RandomProxy(object):

    def process_request(self, request, spider):

        proxy = random.choice(PROXY_LIST)

        print(proxy)

        if 'user_passwd' in proxy:
            # rmb玩家
            b64_up = base64.b64encode(proxy['user_passwd'].encode())

            request.headers['Proxy-Authorization'] = 'Basic ' + b64_up.decode()

            request.meta['proxy'] = proxy['ip_port']
        else:
            # 吃土玩家
            request.meta['proxy'] = proxy['ip_port']