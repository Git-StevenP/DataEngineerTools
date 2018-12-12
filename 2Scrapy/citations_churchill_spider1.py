# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 08:56:43 2018

@author: poulains
"""

import scrapy

class ChurchillQuotesSpider(scrapy.Spider):
    name = "citations de Churchill"
    start_urls = ["http://evene.lefigaro.fr/citations/winston-churchill",]

    def parse(self, response):
        for cit in response.xpath('//li[@class="figsco__selection__list__evene__list__item"]'):
            author_name = cit.css(".figsco__fake__col-9 a::text").extract_first()
            if author_name == 'Winston Churchill':
                text_value = cit.css(".figsco__quote__text a::text").extract_first()
                modifiedText = text_value.replace('“', '').replace('”', '')
                yield { 'text' : modifiedText, 'author' : author_name }
                    
