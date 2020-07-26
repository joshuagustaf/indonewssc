from datetime import datetime

import scrapy


class antara(scrapy.Spider):
    name = 'antara'
    allowed_domains = [
                        'www.antaranews.com'
                      ]
    start_urls = [
                    'https://www.antaranews.com/'
                 ]

    def parse(self, response):
        antaraxpaths = (
                        response.xpath('//*[@id="tab-popular"]/article[1]/header/h3/a/text()').get(),
                        response.xpath('//*[@id="tab-popular"]/article[2]/header/h3/a/text()').get(),
                        response.xpath('//*[@id="tab-popular"]/article[3]/header/h3/a/text()').get(),
                        response.xpath('//*[@id="tab-popular"]/article[4]/header/h3/a/text()').get(),
                        response.xpath('//*[@id="tab-popular"]/article[5]/header/h3/a/text()').get()
                       )
        yield {'Judul (AntaraNews) (1)': antaraxpaths[0],
               'Judul (2)': antaraxpaths[1],
               'Judul (3)': antaraxpaths[2],
               'Judul (4)': antaraxpaths[3],
               'Judul (5)': antaraxpaths[4],
               'Waktu': datetime.now()
               }

