from gc import callbacks
import scrapy
from skalnik_scrap.items import SkalnikScrapItem


class SkalnikEkspresySpider(scrapy.Spider):
    name = 'skalnik_ekspresy'
    allowed_domains = ['www.skalnik.pl']
    start_urls = ['https://www.skalnik.pl/sprzet-wspinaczkowy/wspinaczka/wspinaczka-ekspresy']

    def parse(self, response):
        items = response.css('li.product-item')
        
        scrapper_item = SkalnikScrapItem()
        for item in items:
            prices = item.css('span.price::text').extract()
            scrapper_item['name'] = item.css('a.product-item-link::text').get()
            scrapper_item['price'] = prices[0].replace('\xa0zł', '')
            scrapper_item['old_price'] = None if len(prices) == 1 else prices[1].replace('\xa0zł', '')
            scrapper_item['promo'] = item.css('div.amlabel-text::text').get()
            scrapper_item['url'] = item.css('a.product-item-link').attrib['href']
            yield scrapper_item

        next_page = response.css('[rel="next"] ::attr(href)').get()
        
        if next_page is not None:
            yield response.follow(next_page, callback = self.parse)