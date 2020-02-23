# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyImgItem(scrapy.Item):
    # defined structure of an item, those fields requires those names
    image_urls = scrapy.Field() # needs to be a lists and contains full paths
    images = scrapy.Field()
