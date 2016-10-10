from scrapy import spiders
from tutorial.items import CnBlogSpiderItem
from tutorial import pipelines
# from scrapy.contrib.loader import ItemLoader
import re


class CnBlogSpider(spiders.Spider):

    name = "cnblog"
    allowed_domains = ["cnblog.org"]
    start_urls = [
        'http://www.cnblogs.com/news/'
    ]
    pipeline = set([pipelines.CnBlogSpiderPipeline])

    def parse(self, response):
        for sel in response.xpath('//div[@class="post_item"]')[0:10]:
            item = CnBlogSpiderItem()
            item['title'] = sel.xpath('div/h3/a/text()').extract()
            item['recommended'] = sel.xpath('div/div/span[@class="diggnum"]/text()').extract()[0]
            item['href'] = sel.xpath('div/h3/a/@href').extract()
            item['readed'] = sel.xpath('div/div/span[@class="article_view"]/a/text()').extract()[0].split('(')[1][0:-1]
            yield item
