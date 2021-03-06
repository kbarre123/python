from scrapy.spider import Spider
from scrapy.selector import Selector

from tutorial.items import DmozItem

class DmozSpider(Spider):
    name = "dmoz"
    rotate_user_agent = True #Rotating user agent code taken from https://gist.github.com/seagatesoft/e7de4e3878035726731d
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html
        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []

        for site in sites:
            item = DmozItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('text()').re('-\s[^\n]*\\r')
            items.append(item)
        
        return items