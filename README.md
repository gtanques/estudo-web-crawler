Estrutura:

tutorial/
    scrapy.cfg            # deploy configuration file

    tutorial/             # project's Python module, you'll import your code from here
        __init__.py

        items.py          # project items definition file

        middlewares.py    # project middlewares file

        pipelines.py      # project pipelines file

        settings.py       # project settings file

        spiders/          # a directory where you'll later put your spiders
            __init__.py

--------------------------
Exemplos no scrapy Shell:

>>> response.css('title')
[<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]

>>> response.css('title::text').getall()
['Quotes to Scrape']

>>> response.css('title').getall()
['<title>Quotes to Scrape</title>']

>>> response.css('title::text').get()
'Quotes to Scrape'

>>> response.css('title::text')[0].get()
'Quotes to Scrape'

>>> response.css('title::text').re(r'Quotes.*')
['Quotes to Scrape']

>>> response.css('title::text').re(r'Q\w+')
['Quotes']

>>> response.css('title::text').re(r'(\w+) to (\w+)')
['Quotes', 'Scrape']

>>> response.xpath('//title')
[<Selector xpath='//title' data='<title>Quotes to Scrape</title>'>]

>>> response.xpath('//title/text()').get()
'Quotes to Scrape'

>>> response.css('title')
[<Selector xpath='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]

>>> response.css('title::text').getall()
['Quotes to Scrape']

>>> response.css('title').getall()
['<title>Quotes to Scrape</title>']

>>> quote = response.css("div.quote")[0]

>>> text = quote.css("span.text::text").get()
>>> text
'“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”'

>>> autor=quote.css("small.author::text").get()
>>> autor
'Albert Einstein'

>>> tags = quote.css("div.tags a.tag::text").getall()
>>> tags
['change', 'deep-thoughts', 'thinking', 'world']

-------------------------------------------
>>> for quote in response.css("div.quote"):
...    text = quote.css("span.text::text").get()
...    autor = quote.css("small.author::text").get()
...    tags = quote.css("div.tags a.tag::text").getall()
...    print(dict(text=text, autor=autor, tags=tags)) 
... 
{'text': '“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”', 'autor': 'Albert Einstein', 'tags': ['change', 'deep-thoughts', 'thinking', 'world']}
{'text': '“It is our choices, Harry, that show what we truly are, far more than our abilities.”', 'autor': 'J.K. Rowling', 'tags': ['abilities', 'choices']}
{'text': '“There are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.”', 'autor': 'Albert Einstein', 'tags': ['inspirational', 'life', 'live', 'miracle', 'miracles']}
{'text': '“The person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.”', 'autor': 'Jane Austen', 'tags': ['aliteracy', 'books', 'classic', 'humor']}
{'text': "“Imperfection is beauty, madness is genius and it's better to be absolutely ridiculous than absolutely boring.”", 'autor': 'Marilyn Monroe', 'tags': ['be-yourself', 'inspirational']}
{'text': '“Try not to become a man of success. Rather become a man of value.”', 'autor': 'Albert Einstein', 'tags': ['adulthood', 'success', 'value']}
{'text': '“It is better to be hated for what you are than to be loved for what you are not.”', 'autor': 'André Gide', 'tags': ['life', 'love']}
{'text': "“I have not failed. I've just found 10,000 ways that won't work.”", 'autor': 'Thomas A. Edison', 'tags': ['edison', 'failure', 'inspirational', 'paraphrased']}
{'text': "“A woman is like a tea bag; you never know how strong it is until it's in hot water.”", 'autor': 'Eleanor Roosevelt', 'tags': ['misattributed-eleanor-roosevelt']}
{'text': '“A day without sunshine is like, you know, night.”', 'autor': 'Steve Martin', 'tags': ['humor', 'obvious', 'simile']}