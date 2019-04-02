# -*- coding: utf-8 -*-
import scrapy
from Douban.items import DoubanItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        # print("ua:",response.request.headers['User-Agent'])

        el_list = response.xpath('//*[@class="info"]')

        for el in el_list:
            item = DoubanItem()

            item['name'] = el.xpath('./div[1]/a/span[1]/text()').extract_first()

            yield item


        url = response.xpath('//span[@class="next"]/a/@href').extract_first()
        if url != None:
            url = response.urljoin(url)
            yield scrapy.Request(
                url=url
            )

