# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentProItem

class TencentproSpider(scrapy.Spider):
    name = 'tencentpro'
    # 2.检查修改domain
    allowed_domains = ['tencent.com']
    # 1.修改起始的url
    start_urls = ['https://hr.tencent.com/position.php']

    # 3.编写parse方法
    def parse(self, response):

        # el_list = response.xpath('//*[@id="position"]/div[1]/table/tr')
        el_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        # print(len(el_list))

        for el in el_list:
            item = TencentProItem()

            item['name'] = el.xpath('./td[1]/a/text()').extract_first()
            # urljoin()会自动从当前响应url中获取域名，并且与传入的相对url拼装
            item['link'] = response.urljoin(el.xpath('./td[1]/a/@href').extract_first())
            item['type'] = el.xpath('./td[2]/text()').extract_first()
            item['num'] = el.xpath('./td[3]/text()').extract_first()
            item['address'] = el.xpath('./td[4]/text()').extract_first()
            item['date'] = el.xpath('./td[5]/text()').extract_first()

            # 模拟点击详情页面
            yield scrapy.Request(
                url=item['link'],
                callback=self.parse_detail,
                meta={"itcast": item}
            )

        url = response.xpath('//*[@id="next"]/@href').extract_first()
        if url != 'javascript:;':
            url = response.urljoin(url)
            # req = scrapy.Request(url=url, callback=self.parse)
            req = scrapy.Request(url=url)
            yield req

    def parse_detail(self, response):
        item = response.meta['itcast']

        item['duty'] = ''.join(response.xpath('//tr[3]/td/ul/li/text()').extract())
        item['require'] = ''.join(response.xpath('//tr[4]/td/ul/li/text()').extract())
        # item['duty'] = response.xpath('//tr[3]/td/ul/li/text()').extract_first()
        # item['require'] = response.xpath('//tr[4]/td/ul/li/text()').extract_first()

        yield item
