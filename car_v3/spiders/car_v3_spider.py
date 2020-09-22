# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from car_v3.items import CarV3Item

class CarV3SpiderSpider(CrawlSpider):
    name = 'car_v3_spider'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/4851-1.html']

    rules = (
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/4851-1.html'), callback='parse_page', follow=False),
    )

    def parse_page(self, response):
        car_name = response.xpath("//div[@class='cartab-title']/h2/a/text()").get()
        print('='*30)
        print(car_name)
        print('=' * 30)
        cate = response.xpath("//div[@class='uibox']/div/text()").get()
        urls = response.xpath("//div[@class='uibox']/div[@class='uibox-con carpic-list03 border-b-solid']/ul/li/a/img/@src").getall()
        urls = list(map(lambda url:response.urljoin(url),urls))
        image_urls = list(map(lambda url: url.replace("240x180_0_q95_c42_autohomecar","1024x0_1_q95_autohomecar"), urls))
        item = CarV3Item(cate=cate,image_urls=image_urls)
        yield item
