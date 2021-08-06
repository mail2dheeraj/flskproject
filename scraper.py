import scrapy as scraper;



class webScrap:
    def __init__(self,url):
        self.url=url;
        print('running1')
        
    def screepUri(self):
        print('running2')
        ab=scraper.Request(url=self.url)
        
        
    def apio(self,responce):
        print('running3')
        print(responce)        