# -*- coding: utf-8 -*-
import scrapy
from imagedownload.items import DownloadItem


class WooyunSpider(scrapy.Spider):
    name = "wooyun"
    allowed_domains = ["www.wooyun.org"]
    start_urls = ['http://www.wooyun.org/bugs.php?page=%d' % i for i in range(1, 2000)]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        buglinks = response.xpath('//div[@class="wybug_date"]/ul/li[2]/a/@href').extract()
        for buglink in buglinks:
            url = 'http://www.wooyun.org/' + buglink
            yield scrapy.Request(url, callback=self.parse_detail)

    def parse_detail(self, response):
        item = DownloadItem()
        image_urls = response.xpath('//p[@class="detail usemasaic"]/a/@href').extract()
        for image_url in image_urls:
            item['image_urls'] = [image_url]    # must is list type
            yield item

