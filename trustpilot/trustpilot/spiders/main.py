from urllib.parse import urljoin
import scrapy
from scrapy import *
from trustpilot.items import TrustpilotItem
from scrapy.loader import ItemLoader

categories_links=[
    'here we put all categories we want to scrap from the website'
]

class MainSpider(scrapy.Spider):
    name = 'main'
    def start_requests(self):
        self.table = categories_links[0]
        yield scrapy.Request(f"https://www.trustpilot.com/categories/{categories_links[0]}")
        categories_links.pop(0)  

    def parse(self, response):
        for item in response.css('.styles_categoryBusinessListWrapper__2H2X5 .styles_businessUnitCard__3nW5f'):
            categories = ''
            adresses = ''
            for categorie in item.css('.styles_categories__c4nU- span::text').getall():
                if categorie is not "\u00b7":
                    categories = categories + ' , ' + categorie
            for address in item.css('.styles_location__3JATO span::text').getall():
                if address is not "\u00a0" and address is not "\u00b7":
                    adresses = categories+ ' , ' + address
            l = ItemLoader(item=TrustpilotItem(), response=response)
            l.add_value('name' , item.css('.styles_businessTitle__1IANo::text').get())
            l.add_value('reviews_number' , item.css('.styles_textRating__19_fv::text').getall()[0])
            l.add_value('score' , item.css('.styles_textRating__19_fv::text').getall()[4])
            l.add_value('categories' , categories)
            l.add_value('adresses' , adresses)
            yield l.load_item()
        next_page_link = urljoin(response.url,response.css('.pagination-link_next__1ld6a::attr(href)').get())
        last_item = response.css('.styles_categoryFilteredResultsBold__7x0f4::text').get().split(' of')[0].split('-')[1]
        total_items = response.css('.styles_categoryFilteredResultsBold__7x0f4::text').get().split('of')[1].split(' ')[1]
        if last_item != total_items:
            yield FormRequest(next_page_link,callback=self.parse)
        else:
            if categories_links != []:
                def spider_closed(self, spider):
                   for exporter in self.exporters:
                       exporter.finish_exporting()
                       
                yield FormRequest(f"https://www.trustpilot.com/categories/{categories_links[0]}",callback=self.parse)
                self.table = categories_links[0]
                categories_links.pop(0)