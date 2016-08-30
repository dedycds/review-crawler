import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["google.com"]
    start_urls = [
        "https://plus.google.com/100190592948388789141/about",
        'https://plus.google.com/+GoogleIndonesia/about'
    ]

    def parse(self, response):
        #filename = response.url.split("/")[-2] + '.html'
        #with open(filename, 'wb') as f:
        #    f.write(response.body)
        for sel in response.xpath("//div[contains(@class, 'Ee') and contains(@class, 'wQ') and contains(@class, 'gLa')]"):
            item = DmozItem()
            item['title'] = sel.xpath("div/div[2]/span/a[contains(@class, 'd-s') and contains(@class, 'ob') and contains(@class, 'tv')]/text()").extract()
            item['rating'] = sel.xpath("count(div/div[2]/div[1]/div/span[contains(@class, 'b-db-ac') and contains(@class, 'b-db-ac-th')])").extract()
            item['desc'] = sel.xpath('div/div[2]/div[2]/div/span/text()').extract()
            #print sel
            yield item