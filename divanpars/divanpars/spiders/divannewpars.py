import scrapy

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/chelyabinsk/category/podvesnye-svetilniki"]

    def parse(self, response):
        divans = response.css('div.LlPhw')
        for divan in divans:
            yield{
                'name' : divan.css('div.lsooF span::text').get(),
                'price' : divan.css('div.pY3d2 span::text').get(),
                'url': response.urljoin(divan.css('a::attr(href)').get())
            }
