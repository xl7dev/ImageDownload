# -*- coding: utf-8 -*-

# Scrapy settings for imagedownload project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'imagedownload'

SPIDER_MODULES = ['imagedownload.spiders']
NEWSPIDER_MODULE = 'imagedownload.spiders'

ITEM_PIPELINES = {
    # 'scrapy.pipelines.images.ImagesPipeline': 1,
    'imagedownload.pipelines.MyImagesPipeline': 1
}
IMAGES_STORE = '/Users/username/ImageDownload/imagedownload'    # replace images save path
# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:21.0) Gecko/20130331 Firefox/21.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
