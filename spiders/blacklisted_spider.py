import scrapy

class BlacklistSpider(scrapy.Spider):
    allowed_domains = ['nfs.punjab.gov.pk']
    name = "blacklisted"

    def start_requests(self):
        urls = [
            'https://nfs.punjab.gov.pk/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        import csv;
        csv.writer(open('blacklisted_ppl_list.csv', 'w')).writerows([tr.css('td::text').getall()[2:3] for tr in response.css('table').css('tr')])
        # tr.css('td::text').getall()[2:2] for tr in response.css('table').css('tr')]
        #print(response)

        #rows = response.css('table.table.table-stripped tbody tr')
        #for row in rows:
         #   print(row.css('td')[0])




