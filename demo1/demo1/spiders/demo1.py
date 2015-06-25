from scrapy import Spider
from scrapy.selector import Selector
'''from demo1.items import Demo1Item'''
item={}
class demo1(Spider):
	name="demo1"
	allowed_domains=['stackoverflow.com']
	start_urls=['http://stackoverflow.com/questions/tagged/python']
	def parse(self,response):
		
		questions=Selector(response).xpath("//div[@class='summary']/h3")
		for question in questions:
			'''item=Demo1Item()'''
			item['title'] = question.xpath('a[@class="question-hyperlink"]/text()').extract()[0]
			print  item['title']

