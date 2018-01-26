# -*- coding: utf-8 -*-

# Scrapy settings for webscrapper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'webscrapper'

SPIDER_MODULES = ['webscrapper.spiders']
NEWSPIDER_MODULE = 'webscrapper.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'webscrapper (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

FEED_URI = 'logs/%(time)s_movies.json'
FEED_FORMAT = 'json'

# Configure item pipelines
ITEM_PIPELINES = {
   'webscrapper.pipelines.WebscrapperPipeline': 300,
}