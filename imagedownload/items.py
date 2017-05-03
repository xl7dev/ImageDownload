# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DownloadItem(scrapy.Item):
    image_urls = scrapy.Field()  # 图片连接
    images = scrapy.Field()  # 图片下载结果
