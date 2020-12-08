import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    # Verbose method:
    # def start_requests(self):
    #     urls=[
    #         'http://quotes.toscrape.com/page/1/',
    #         'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = f'quotes-{page}.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    #     self.log(f'Saved file {filename}')

    # Clean Method
    # O método parse () será chamado para lidar com cada uma das solicitações para esses URLs,
    #  embora não tenhamos dito explicitamente a Scrapy para fazer isso.
    #  Isso acontece porque parse () é o método de retorno de chamada padrão do Scrapy,
    #  que é chamado para solicitações sem um retorno de chamada explicitamente atribuído.
    # 
    # class QuotesSpider(scrapy.Spider):
    #     name = "quotes"
    # start_urls = [
    #     'http://quotes.toscrape.com/page/1/',
    #     'http://quotes.toscrape.com/page/2/',
    # ]
    # def parse(self, response):
    #     page = response.url.split("/")[-2]
    #     filename = f'quotes-{page}.html'
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    # Verbose
    # class QuotesSpider(scrapy.Spider):
    #     name = "quotes"
    # start_urls = [
    #     'http://quotes.toscrape.com/page/1/',
    #     'http://quotes.toscrape.com/page/2/',
    # ]

    # def parse(self, response):
    #     for quote in response.css("div.quote"):
    #         yield{
    #             'text' : quote.css('span.text::text').get(),
    #             'autor' : quote.css('small.author::text').get(),
    #             'tags' : quote.css('div.tags a.tag::text').getall(),
    #         }        

    #     next_page = response.css('li.next a::attr(href)').get()
    #     if next_page is not None:
    #         next_page = response.urljoin(next_page)
    #         yield scrapy.Request(next_page, callback=self.parse)

# Um atalho para a criação de solicitações               
# Ao contrário de scrapy.Request, response.follow suporta URLs relativos diretamente 
# não há necessidade de chamar urljoin. Observe que response.follow apenas retorna uma
#  instância de Request; você ainda tem que render este pedido.

    # def parse(self, response):
    #     for quote in response.css('div.quote'):
    #         yield {
    #             'text': quote.css('span.text::text').get(),
    #             'author': quote.css('span small::text').get(),
    #             'tags': quote.css('div.tags a.tag::text').getall(),
    #         }
# Para criar várias solicitações de um iterável, você pode usar response.follow_all em vez disso:
# anchors = response.css('ul.pager a')
# yield from response.follow_all(anchors, callback=self.parse)
# ou, encurtando ainda mais:
# yield from response.follow_all(css='ul.pager a', callback=self.parse)
        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)     

    def start_requests(self):
        url = 'http://quotes.toscrape.com/'
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)