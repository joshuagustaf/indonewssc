from datetime import datetime

import scrapy


class linetodaynews(scrapy.Spider):
    name = 'linetoday'
    allowed_domains = [
                        'www.today.line.me'
                      ]
    start_urls = [
                    'https://today.line.me/ID/pc/popular/100270'
                 ]
    def parse(self, response):
        linetodxpaths = (
                        response.xpath('//*[@id="container"]/div/ol/li[1]/a/div/p/text()').extract(),
                        response.xpath('//*[@id="container"]/div/ol/li[2]/a/div/p/text()').extract(),
                        response.xpath('//*[@id="container"]/div/ol/li[3]/a/div/p/text()').extract(),
                        response.xpath('//*[@id="container"]/div/ol/li[4]/a/div/p/text()').extract(),
                        response.xpath('//*[@id="container"]/div/ol/li[5]/a/div/p/text()').extract(),
                        response.xpath('//*[@id="container"]/div/ol/li[6]/a/div/p/text()').extract(),
                        response.xpath('//*[@id="container"]/div/ol/li[7]/a/div/p/text()').extract(),
                        response.xpath('//*[@id="container"]/div/ol/li[8]/a/div/p/text()').extract(),
                        response.xpath('//*[@id="container"]/div/ol/li[9]/a/div/p/text()').extract(),
                        response.xpath('//*[@id="container"]/div/ol/li[10]/a/div/p/text()').extract()
                        )
        yield { 'Judul (LINE TODAY) (1)' : linetodxpaths [0],
                'Judul (2)' : linetodxpaths [1],
                'Judul (3)' : linetodxpaths [2],
                'Judul (4)' : linetodxpaths [3],
                'Judul (5)' : linetodxpaths [4],
                'Judul (6)' : linetodxpaths [5],
                'Judul (7)' : linetodxpaths [6],
                'Judul (8)' : linetodxpaths [7],
                'Judul (9)' : linetodxpaths [8],
                'Judul (10)': linetodxpaths [9],
                'Waktu': datetime.now()
              }
