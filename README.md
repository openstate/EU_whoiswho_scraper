# EU Whoiswho Scraper

Scrapy spider to scrape the data of people listed on the [EU Whoiswho](http://europa.eu/whoiswho/public/) website.

If you're looking for the dataset, go to [this page](https://github.com/openstate/datasets/tree/master/eu_whoiswho).

## Instructions
* Clone this repository or simply download the python files
* Install [Scrapy](http://scrapy.org/)
* Run the following command to start scraping (the whole website takes 9 hours to scrape!):
```
    scrapy runspider spider.py -o data.json
```
* (optional) run `json2csv.py` to convert the results from `data.json` to `data.csv`
