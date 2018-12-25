# -*- coding: utf-8 -*-
import scrapy

from inxeduCrawer.items import PicItem



class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/list-1-1.html']

    def parse(self, response):
        allPics=response.xpath("//div[@class='img']/a");
        for pic in allPics:
            # 分别处理每个图片，取出名称及地址
            item = PicItem()
            name = pic.xpath('./img/@alt').extract()[0]
            addr = pic.xpath('./img/@src').extract()[0]
            addr = 'http://www.xiaohuar.com' + addr
            item['name'] = name
            item['addr'] = addr
            # 返回爬取到的数据
            yield item