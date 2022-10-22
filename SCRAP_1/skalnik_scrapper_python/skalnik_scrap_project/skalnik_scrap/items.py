# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SkalnikScrapItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    old_price = scrapy.Field()
    promo = scrapy.Field()
    url = scrapy.Field()