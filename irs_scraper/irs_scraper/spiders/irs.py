import scrapy


class PoetrySpider(scrapy.Spider):
    name = 'tax_scraper'
    start_urls = ['https://www.irs.gov/efile-index-taxpayer-search?zip=10001&state=35&page=1']

    def parse(self, response):
        # zip_code = input('Enter ZIP Code')
        # state = ['Alabama', 'Alaska', 'American Samoa', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
        #          'Delaware', 'District of Columbia', 'Florida', 'Georgia', 'Guam',
        #          'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine',
        #          'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Northern Mariana', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania', 'Puerto Rico', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 'Virgin Islands', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming', ]
        try:
            for poem in response.css('div.view-content'):
                yield {
                    'Name of Business': poem.css('td.views-field.views-field-nothing-1.views-align-left').getall().split('\n')[0].replace('<td class="views-field views-field-nothing-1 views-align-left">', ''),
                    'Address': poem.css('td.views-field.views-field-nothing-1.views-align-left').getall().split('\n')[1],
                    'City/State/ZIP': poem.css('td.views-field.views-field-nothing-1.views-align-left').getall().split('\n')[2],
                    'Point of Contact': poem.css('td.views-field.views-field-nothing-1.views-align-left').getall().split('\n')[3],
                    'Telephone': poem.css('td.views-field.views-field-nothing-1.views-align-left').getall().split('\n')[4][4:-4],
                    'Type of Service': poem.css('td.views-field.views-field-nothing-1.views-align-left').getall().split('\n')[3],
                }

            next_page = response.css('a[rel="next"]::attr(href)').get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
        except Exception as e:
            print(e)
            pass
