# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import scrapy




class LkmlPatch(scrapy.Item):
    diff=scrapy.Field()
    patch_md5=scrapy.Field()
    signed_off=scrapy.Field()

class LkmlPost(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #Date = parse("Mon, 1 Jan 1000  00:00:00 +0000")    
    Date=scrapy.Field()
    From=scrapy.Field()
    Subject=scrapy.Field()
    post_id=scrapy.Field()
    Body=scrapy.Field()
    Parent_id=scrapy.Field()
    patches=scrapy.Field()
    
