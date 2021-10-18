import scrapy


class Whiskyspider(scrapy.Spider):
    name = 'Whiskyspider'
    start_urls = ['https://www.whiskyshop.com/catalogsearch/result/?q=scotch']

    def parse(self, response):
        for p in response.css('div.product-item-info'):
            try:
                yield {

                    'name': p.css('a.product-item-link::text').get(),
                    'price': p.css('span.price::text').get().replace('£', ''),
                    'link': p.css('a.product-item-link').attrib['href']
                }
            except:
                {

                    'name': p.css('a.product-item-link::text').get(),
                    'price': 'sold out',
                    'link': p.css('a.product-item-link').attrib['href']
                }
        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
