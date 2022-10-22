# skalnik_scrapper_python
Scrapy project, designed to scrap informations about selected category of products (from website www.skalnik.pl) and compare them in json format

Current functionalities:
Spider: skalnik_ekspresy - crawl through category 'ekspresy' and lists each product with name, price, promotion, price before promotion and url
json_comparer.py - script to compare two latest files created by spider skalnik_ekspresy, prints all products with occured differences 
json_store - directory to store json files created by spider 
