# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['JD.spiders']
NEWSPIDER_MODULE = 'JD.spiders'

USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

# 设定重复过滤器类，如果不设定，默认使用普通python的集合，如果设置为scrapy——redis的组件，将会使用redis数据库中的集合
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 替换scrapy中调度器组件
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 设置当爬虫运行中断时，任务队列是否保持，设置之后，爬虫退出，远程redis将会继续保持任务队列以及去重集合
SCHEDULER_PERSIST = True
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    # 'JD.pipelines.ExamplePipeline': 300,
    # 设置该管道之后，数据将会自动保存到redis数据库的一个数据队列中
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
DOWNLOAD_DELAY = 1

REDIS_URL = "redis://172.16.123.223:6379"










# # -*- coding: utf-8 -*-
#
# # Scrapy settings for JD project
# #
# # For simplicity, this file contains only settings considered important or
# # commonly used. You can find more settings consulting the documentation:
# #
# #     http://doc.scrapy.org/en/latest/topics/settings.html
# #     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# #     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#
# BOT_NAME = 'JD'
#
# SPIDER_MODULES = ['JD.spiders']
# NEWSPIDER_MODULE = 'JD.spiders'
#
#
# # Crawl responsibly by identifying yourself (and your website) on the user-agent
# #USER_AGENT = 'JD (+http://www.yourdomain.com)'
#
# # Obey robots.txt rules
# ROBOTSTXT_OBEY = True
#
# # Configure maximum concurrent requests performed by Scrapy (default: 16)
# #CONCURRENT_REQUESTS = 32
#
# # Configure a delay for requests for the same website (default: 0)
# # See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# # See also autothrottle settings and docs
# #DOWNLOAD_DELAY = 3
# # The download delay setting will honor only one of:
# #CONCURRENT_REQUESTS_PER_DOMAIN = 16
# #CONCURRENT_REQUESTS_PER_IP = 16
#
# # Disable cookies (enabled by default)
# #COOKIES_ENABLED = False
#
# # Disable Telnet Console (enabled by default)
# #TELNETCONSOLE_ENABLED = False
#
# # Override the default request headers:
# #DEFAULT_REQUEST_HEADERS = {
# #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# #   'Accept-Language': 'en',
# #}
#
# # Enable or disable spider middlewares
# # See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# #SPIDER_MIDDLEWARES = {
# #    'JD.middlewares.JdSpiderMiddleware': 543,
# #}
#
# # Enable or disable downloader middlewares
# # See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# #DOWNLOADER_MIDDLEWARES = {
# #    'JD.middlewares.MyCustomDownloaderMiddleware': 543,
# #}
#
# # Enable or disable extensions
# # See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# #EXTENSIONS = {
# #    'scrapy.extensions.telnet.TelnetConsole': None,
# #}
#
# # Configure item pipelines
# # See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# #ITEM_PIPELINES = {
# #    'JD.pipelines.JdPipeline': 300,
# #}
#
# # Enable and configure the AutoThrottle extension (disabled by default)
# # See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# #AUTOTHROTTLE_ENABLED = True
# # The initial download delay
# #AUTOTHROTTLE_START_DELAY = 5
# # The maximum download delay to be set in case of high latencies
# #AUTOTHROTTLE_MAX_DELAY = 60
# # The average number of requests Scrapy should be sending in parallel to
# # each remote server
# #AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# # Enable showing throttling stats for every response received:
# #AUTOTHROTTLE_DEBUG = False
#
# # Enable and configure HTTP caching (disabled by default)
# # See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# #HTTPCACHE_ENABLED = True
# #HTTPCACHE_EXPIRATION_SECS = 0
# #HTTPCACHE_DIR = 'httpcache'
# #HTTPCACHE_IGNORE_HTTP_CODES = []
# #HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
