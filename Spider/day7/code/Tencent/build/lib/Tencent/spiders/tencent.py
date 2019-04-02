# -*- coding: utf-8 -*-
import scrapy


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    # 2 检查修改
    allowed_domains = ['tencent.com']
    # 1 修改起始的url
    start_urls = ['https://hr.tencent.com/position.php?&start=']

    def parse(self, response):
        el_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        print(len(el_list))

        for el in el_list:
            temp = {}

            temp['name'] = el.xpath('./td[1]/a/text()').extract_first()
            # temp['link'] = el.xpath('./td[1]/a/@href').extract_first()
            temp['link'] = response.urljoin(el.xpath('./td[1]/a/@href').extract_first())
            temp['class'] = el.xpath('./td[2]/text()').extract_first()
            temp['num'] = el.xpath('./td[3]/text()').extract_first()
            temp['address'] = el.xpath('./td[4]/text()').extract_first()
            temp['pub_date'] = el.xpath('./td[5]/text()').extract_first()
            yield temp

        # 模拟翻页
        # 获取url
        # url = "https://hr.tencent.com/" + response.xpath('//*[@id="next"]/@href')
        partial_url = response.xpath('//*[@id="next"]/@href').extract_first()

        if partial_url != "javascript:;":
            # 自动补全相对路径的url
            url = response.urljoin(partial_url)

            # 构建请求对象，返回给引擎
            yield scrapy.Request(url,callback=self.parse)