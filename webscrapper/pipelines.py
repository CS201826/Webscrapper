# -*- coding: utf-8 -*-

# Define your item pipelines here
#
import re

class WebscrapperPipeline(object):
	def strip_tags(self, value):
		data = ''
		if value is not None:
			data = re.sub(r'[?,(,),.,\t,\n,\r, " "]', '', value)
		return data
	
	def process_item(self, item, spider):
		item['rank'] = self.strip_tags(item['rank'])
		item['year'] = self.strip_tags(item['year'])
		return item
