# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# Extracted data --> Temporary containers (items) --> Storing in dtabase 

import scrapy 

class EmpireItem(scrapy.Item):

    ids = scrapy.Field()
    niche = scrapy.Field()
    monetization = scrapy.Field()
    price = scrapy.Field()
    net = scrapy.Field()
    multiple = scrapy.Field()
    pricing_period = scrapy.Field()
    monthly_revenue = scrapy.Field()
    hrs_worked_per_week = scrapy.Field()
    platfrom = scrapy.Field()
    domain_type = scrapy.Field()
    year_created = scrapy.Field()
    page_views = scrapy.Field()
    unique_users = scrapy.Field()