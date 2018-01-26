#Coding: utf-8

#Import Libraries
import os
import scrapy
from webscrapper.items import WebscrapperItem

#Get Current file path
_dir = os.path.dirname(os.path.abspath(__file__))

class Movies(scrapy.Spider):
	"""
	This class is inherited from Spider to get all Top rated movies
	and save as json format
	"""
	name = "movies"
	start_urls = ["http://www.imdb.com"]

	def parse(self, response):
		""" Parse url to fetch content"""
		wrapper = response.xpath('//div[@id="navbar"]/div[@id="megaMenu"]')

		# Get all Menus
		for top_menu in wrapper.xpath('//ul/li[@id="navTitleMenu"]'):

			# Get Top rated movies Menu item 
			for sub_menu in top_menu.xpath('//div[@class="subNavListContainer"]/ul/li/a[text()="Top Rated Movies"]/@href'):
				url = sub_menu.extract()
				yield scrapy.Request(response.urljoin(url), callback=self.parse_dir_contents)

	def parse_dir_contents(self, response):
		item = WebscrapperItem()
		rows = response.xpath('//table/tbody[@class="lister-list"]/tr')

		# Fetch all table elements
		for index in range(len(rows)):
			item['rank'] = response.xpath('//table/tbody[@class="lister-list"]/tr['+str(index+1)+']/td[@class="titleColumn"]/text()')[0].extract()			
			item['title'] = response.xpath('//table/tbody[@class="lister-list"]/tr['+str(index+1)+']/td[@class="titleColumn"]/a/text()')[0].extract()
			item['year'] = response.xpath('//table/tbody[@class="lister-list"]/tr['+str(index+1)+']/td[@class="titleColumn"]/span/text()')[0].extract()
			item['rating'] = response.xpath('//table/tbody[@class="lister-list"]/tr['+str(index+1)+']/td[contains(@class, "ratingColumn") and contains(@class, " imdbRating")]/strong/text()')[0].extract()
			yield item