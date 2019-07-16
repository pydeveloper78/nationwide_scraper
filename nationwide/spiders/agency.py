# -*- coding: utf-8 -*-
import scrapy


class AgencySpider(scrapy.Spider):
    name = 'agency'
    allowed_domains = ['agency.nationwide.com']
    start_urls = ['http://agency.nationwide.com/']

    def parse(self, response):
        for url in response.xpath('//a[@class="Directory-listLink"]/@href').extract():
            yield scrapy.Request(response.urljoin(url))
        for row in response.xpath('//li[contains(@class,"Directory-listTeaser--single")]/article'):
            item = {}
            item['company_name'] = row.xpath('//span[@id="location-name"]/text()').extract_first()
            item['name'] = row.xpath('//div[@class="Teaser-agentName"]/text()').extract_first()
            item['phone'] = row.xpath('//span[@itemprop="telephone"]/text()').extract_first()
            item['address'] = row.xpath('//span[@class="c-address-street-1"]/text()').extract_first()
            item['city'] = row.xpath('//span[@class="c-address-city"]/text()').extract_first()
            item['state'] = row.xpath('//abbr[@itemprop="addressRegion"]/text()').extract_first()
            item['zipcode'] = row.xpath('//span[@itemprop="postalCode"]/text()').extract_first()
            yield item