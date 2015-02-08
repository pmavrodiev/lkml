import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from lkml.items import LkmlPatch, LkmlPost
from scrapy.selector import Selector

class lkmlSpider(CrawlSpider):
    name = 'lkmlSpider'
    allowed_domains = ['lkml.org']
    start_urls = ['https://lkml.org/lkml']

    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(LinkExtractor(allow=('category\.php', ), deny=('subsection\.php', ))),

        # Extract links matching 'item.php' and parse them with the spider's method parse_item
        Rule(LinkExtractor(allow=('item\.php', )), callback='parse_item'),
    )

    def parse_item(self, response):
        self.log('Hi, this is an item page! %s' % response.url)
        item = scrapy.Item()
        item['id'] = response.xpath('//td[@id="item_id"]/text()').re(r'ID: (\d+)')
        item['name'] = response.xpath('//td[@id="item_name"]/text()').extract()
        item['description'] = response.xpath('//td[@id="item_description"]/text()').extract()
        return item
      

class simpleSpider(scrapy.Spider):
    name = 'simpleSpider'
    allowed_domains = ['lkml.org']
    start_urls = ['https://lkml.org/lkml/2006/1/8/2']    
    
    def parse(self, response):
	sel = Selector(response)
        for h3 in response.xpath('//h3').extract():
            yield MyItem(title=h3)

        for url in response.xpath('//a/@href').extract():
            yield scrapy.Request(url, callback=self.parse)
            
            
   