import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from lkml.items import LkmlPatch, LkmlPost
from scrapy.selector import Selector
from dateutil.parser import *
from dateutil.tz import *
from datetime import *


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
    start_urls = ['https://lkml.org/lkml/2015/2/4/6']    
    
    def parse(self, response):
	#XPATH parsing
	dateText=response.xpath("//table/tr/td[@itemprop='datePublished']/text()").extract()
	if len(dateText)==0:
	  print "Could not match the Date of the post"
	authorText=response.xpath("//table/tr/td[@itemprop='author']/text()").extract()
	if len(authorText)==0:
	  print "Coult not match the Author of the post"
	subjectText=response.xpath("//table/tr/td[@itemprop='name']/text()").extract()
	if len(subjectText)==0:
	  print "Coult not match the Subject of the post"
	postBody=response.xpath("//pre[@itemprop='articleBody']").extract()
	if len(postBody)==0:
	  print "Could not match the Body of the post"	 
	#create the scrapy item LkmlPost
	post=LkmlPost()
	post["Date"]=parse(dateText[0])
	post["From"]=authorText[0]
	post["Subject"]=subjectText[0]
	post["Body"]=postBody[0]
	#The logic continues by noticing that often the e-mail is not included in the From field, only the name.
	#So scan the articleBody for the same name and extract the associated email.
	#Some places to look for in articleBody are signed-off-by bits or simply blind text search for the name.
	print response.body
	
        #for h3 in response.xpath('//h3').extract():
        #    yield MyItem(title=h3)

        #for url in response.xpath('//a/@href').extract():
        #    yield scrapy.Request(url, callback=self.parse)
            
            
   