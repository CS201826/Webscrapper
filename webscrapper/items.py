# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebscrapperItem(scrapy.Item):
    # define the fields for spider
    rank = scrapy.Field()
    title = scrapy.Field()
    rating = scrapy.Field()
    year = scrapy.Field()