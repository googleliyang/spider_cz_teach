# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem


class TencentproSpider(scrapy.Spider):
    name = 'tencentpro'
    # -*- coding: utf-8 -*-
    import scrapy
    allowed_domains = ['tencent.com']
    # 1 修改起始的url
    start_urls = ['https://hr.tencent.com/position.php?&start=']

    def parse(self, response):
        el_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        print(len(el_list))

        for el in el_list:
            temp = TencentItem()

            temp['name'] = el.xpath('./td[1]/a/text()').extract_first()
            # temp['link'] = el.xpath('./td[1]/a/@href').extract_first()
            temp['link'] = response.urljoin(el.xpath('./td[1]/a/@href').extract_first())
            temp['category'] = el.xpath('./td[2]/text()').extract_first()
            temp['num'] = el.xpath('./td[3]/text()').extract_first()
            temp['address'] = el.xpath('./td[4]/text()').extract_first()
            temp['pub_date'] = el.xpath('./td[5]/text()').extract_first()

            # meta传递的数据将会出现在callback指定的解析方法中，存在于response中
            yield scrapy.Request(url=temp['link'],callback=self.parse_detail,meta={"python19":temp})

        # 模拟翻页
        # 获取url
        # url = "https://hr.tencent.com/" + response.xpath('//*[@id="next"]/@href')
        partial_url = response.xpath('//*[@id="next"]/@href').extract_first()

        if partial_url != "javascript:;":
            # 自动补全相对路径的url
            url = response.urljoin(partial_url)

            # 构建请求对象，返回给引擎
            yield scrapy.Request(url, callback=self.parse)

    def parse_detail(self, response):
        temp=response.meta['python19']

        # 补全数据
        temp['duty'] = ''.join(response.xpath('//tr[3]/td/ul/li/text()').extract())
        temp['requirement'] = ''.join(response.xpath('//tr[4]/td/ul/li/text()').extract())
        yield temp