import scrapy

class Teia(scrapy.Spider):
    nome= 'QuotesSpider'
    start_urls = ['http://quotes.toscrape.com/']
    
    def parse(self,response):
        quotes = response.xpath('*//div[@class="quote"]')
        for i in quotes: