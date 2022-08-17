import scrapy


class PoetrySpider(scrapy.Spider):
    name = 'poetry'
    start_urls = ['https://shayariurdu.com/zindagi-shayari/',
                  'https://shayariurdu.com/yaad-poetry/',
                  'https://shayariurdu.com/wasi-shah-poetry/',
                  'https://shayariurdu.com/wafa-shayari/',
                  'https://shayariurdu.com/urdu-shayari-mohabbat/',
                  'https://shayariurdu.com/urdu-sms-poetry-sms/',
                  'https://shayariurdu.com/urdu-poetry-images/',
                  'https://shayariurdu.com/urdu-motivational-poetry/',
                  'https://shayariurdu.com/urdu-love-poetry/',
                  'https://shayariurdu.com/two-line-shayari/',
                  'https://shayariurdu.com/tehzeeb-hafi-poetry/',
                  'https://shayariurdu.com/teachers-day-shayari/',
                  'https://shayariurdu.com/tanha-shayari/',
                  'https://shayariurdu.com/sufi-shayari/',
                  'https://shayariurdu.com/sorry-shayari/',
                  'https://shayariurdu.com/shikwa-poetry/',
                  'https://shayariurdu.com/shayari-on-waqt/',
                  'https://shayariurdu.com/shayari-on-life/',
                  'https://shayariurdu.com/shayari-gif/',
                  'https://shayariurdu.com/shadi-shayari/',
                  'https://shayariurdu.com/sana-ahmed-poetry/',
                  'https://shayariurdu.com/saghar-siddiqui-poetry/',
                  'https://shayariurdu.com/sad-urdu-poetry/',
                  'https://shayariurdu.com/romantic-urdu-poetry/',
                  'https://shayariurdu.com/qaiser-ul-jafri-shayari/']

    def parse(self, response):
        try:
            for poem in response.css('div.entry-content'):
                yield {
                    'image-link': poem.css('img').attrib['src'],
                }

            next_page = response.css('a.next').attrib['href']
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
        except Exception as e:
            print(e)
            pass
