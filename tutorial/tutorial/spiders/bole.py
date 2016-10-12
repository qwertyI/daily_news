from scrapy import spiders
from tutorial.items import BoleSpiderItem
from tutorial import pipelines
# from scrapy.contrib.loader import ItemLoader
import re


class BoleSpider(spiders.Spider):

    name = "bole"
    allowed_domains = ["bole.org"]
    start_urls = [
        'http://python.jobbole.com/all-posts/'
    ]
    pipeline = set([pipelines.BoleSpiderPipeline])

    def parse(self, response):
        title = []
        for sel in response.xpath('//div[@class="post floated-thumb"]')[0:10]:
            item = BoleSpiderItem()
            item['title'] = sel.xpath('div/p/a/text()').extract()
            title.append(item['title'][0])
            item['img'] = sel.xpath('div/a/img/@src').extract()
            item['href'] = sel.xpath('div/p/a/@href').extract()
            yield item
        k = 1
        for i in title:
            print str(k) + ' : ' + i
            k += 1
