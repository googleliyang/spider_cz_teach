# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TencentSpider(CrawlSpider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    rules = (
        # 编写详情页面的链接提取规则
        # Rule(LinkExtractor(allow=r'position_detail.php\?id=\d+&keywords=&tid=0&lid=0'), callback='parse_item'),
        # follow决定是否在链接提取器提取的链接对应的响应中继续应用该规则
        Rule(LinkExtractor(allow='position.php\?&start=\d+#a'), follow=True, callback='parse_item'),
    )

    def parse_item(self, response):
        print(response.url)



# crawlspider 爬虫的使用范围
#     所有的数据都在一个响应中就能提取
#     对于爬取性能要求比较搞