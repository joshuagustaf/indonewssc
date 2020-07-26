from datetime import datetime

import scrapy


class detikdotcom(scrapy.Spider):
    name = 'detik'
    allowed_domains = [
                        'www.detik.com'
                      ]
    start_urls = [
                    'https://www.detik.com/'
                 ]

    def parse(self, response):
        detikxpaths = (
                        response.xpath('/html/body/div[6]/div/div[3]/div[7]/div[2]/article[1]/div/div[1]/h3/a/text()').get(),
                        response.xpath('/html/body/div[6]/div/div[3]/div[7]/div[2]/article[2]/div/div[1]/h3/a/text()').get(),
                        response.xpath('/html/body/div[6]/div/div[3]/div[7]/div[2]/article[3]/div/div[1]/h3/a/text()').get(),
                        response.xpath('/html/body/div[6]/div/div[3]/div[7]/div[2]/article[4]/div/div[1]/h3/a/text()').get(),
                        response.xpath('/html/body/div[6]/div/div[3]/div[7]/div[2]/article[5]/div/div[1]/h3/a/text()').get()
                       )
        yield {'Judul (Detik) (1)': detikxpaths[0],
               'Judul (2)': detikxpaths[1],
               'Judul (3)': detikxpaths[2],
               'Judul (4)': detikxpaths[3],
               'Judul (5)': detikxpaths[4],
               'Waktu': datetime.now()
               }

