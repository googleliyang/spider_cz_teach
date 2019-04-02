# -*- coding: utf-8 -*-
import scrapy
from JD.items import JdItem
import json
# ----1 导入
from scrapy_redis.spiders import RedisSpider


# ----2 修改继承
class BookSpider(RedisSpider):
    name = 'book'

    # ----3 注销
    # allowed_domains = ['jd.com','p.3.cn']
    # start_urls = ['https://book.jd.com/booksort.html']

    # ----4 redis-key
    redis_key = 'py37'

    # ----5 __init__
    def __init__(self, *args, **kwargs):
        domain = kwargs.pop("domain","")
        self.allowed_domains = list(filter(None, domain.split(',')))
        super(BookSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        # 获取所有大分类节点列表
        big_node_list = response.xpath('//*[@id="booksort"]/div[2]/dl/dt/a')

        for big_node in big_node_list[:1]:
            big_category = big_node.xpath('./text()').extract_first()
            big_category_link = response.urljoin(big_node.xpath('./@href').extract_first())

            small_node_list = big_node.xpath('../following-sibling::dd[1]/em/a')
            for small_node in small_node_list[:1]:

                temp = {}
                temp['small_category'] = small_node.xpath('./text()').extract_first()
                temp['small_category_link'] = response.urljoin(small_node.xpath('./@href').extract_first())
                temp['big_category'] = big_category
                temp['big_category_link'] = big_category_link

                yield scrapy.Request(
                    url=temp['small_category_link'],
                    callback=self.parse_book_list,
                    meta={'meta_1': temp}
                )

    def parse_book_list(self, response):

        temp = response.meta['meta_1']

        # 获取所有的图书节点列表
        book_list = response.xpath('//*[@id="plist"]/ul/li/div')
        # print(len(book_list))

        for book in book_list:

            item = JdItem()

            item['big_category'] = temp['big_category']
            item['big_category_link'] = temp['big_category_link']
            item['small_category'] = temp['small_category']
            item['small_category_link'] = temp['small_category_link']

            item['bookname'] = book.xpath('./div[3]/a/em/text()|./div/div[2]/div[1]/div[3]/a/em/text()').extract_first()
            item['author'] = book.xpath('./div[4]/span[1]/span/a/text()|//*[@id="plist"]/ul/li[28]/div/div/div[2]/div[1]/div[4]/span[1]/span/a/text()').extract_first()
            item['cover_link'] = response.urljoin(book.xpath('./div[1]/a/img/@src|./div[1]/a/img/@data-lazy-img').extract_first())
            item['detail_link'] = response.urljoin(book.xpath('./div[1]/a/@href').extract_first())

            # 获取价格
            skuid = book.xpath('./@data-sku|./div/div[2]/div[1]/@data-sku').extract_first()
            url = 'https://p.3.cn/prices/mgets?skuIds=J_' + skuid

            yield scrapy.Request(
                url=url,
                callback=self.parse_price,
                meta={'meta_2':item}
            )

    def parse_price(self, response):

        item = response.meta['meta_2']

        item['price'] = json.loads(response.body)[0]['op']

        yield item









