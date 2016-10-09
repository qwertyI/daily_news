from scrapy import spiders
from tutorial.items import TesterhomeSpiderItem
from tutorial import pipelines
# from scrapy.contrib.loader import ItemLoader
import re


class TesterhomeSpider(spiders.Spider):

    name = "testerhome"
    allowed_domains = ["testerhome.org"]
    start_urls = [
        'http://testerhome.com'
    ]
    pipeline = set([pipelines.TesterhomeSpiderPipeline])

    def parse(self, response):
        for sel in response.xpath('//div[contains(@class,"topic media topic")]')[0:10]:
            item = TesterhomeSpiderItem()
            item['topic_title'] = sel.xpath('div/div[contains(@class,"title media-heading")]/a/text()').extract()
            item['topic_href'] = [self.start_urls[0] + sel.xpath('div/div[contains(@class,"title media-heading")]/a/@href').extract()[0]]
            item['topic_author'] = sel.xpath('div/div[contains(@class,"info")]/a/@data-name').extract()
            item['topic_class'] = sel.xpath('div/div[contains(@class,"info")]/a[contains(@class,"node")]/text()').extract()
            item['topic_reply_num'] = sel.xpath('div[contains(@class,"count media-right")]/a/text()').extract()
            item['topic_author_img'] = sel.xpath('div/a/img/@src').extract()
            yield item

