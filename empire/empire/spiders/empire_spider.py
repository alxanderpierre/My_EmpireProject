
import scrapy
from empire.items import EmpireItem
import re
import scrapy.spiders

from lxml.html import fromstring
import requests
from itertools import cycle
import traceback




class EmpireSpider(scrapy.Spider):
    name = 'empire'
    start_urls = [
        "https://empireflippers.com/marketplace/"
    ]

    # def get_proxies():
    #     url = 'https://free-proxy-list.net/'
    #     response = requests.get(url)
    #     parser = fromstring(response.text)
    #     proxies = set()
    #     for i in parser.xpath('//tbody/tr')[:10]:
    #         if i.xpath('.//td[7][contains(text(),"yes")]'):
    #             proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
    #             proxies.add(proxy)
    #     return proxies


    # #If you are copy pasting proxy ips, put in the list below
    # #proxies = ['121.129.127.209:80', '124.41.215.238:45169', '185.93.3.123:8080', '194.182.64.67:3128', '106.0.38.174:8080', '163.172.175.210:3128', '13.92.196.150:8080']

    # proxies = get_proxies()
    # proxy_pool = cycle(proxies)

    # url = 'https://httpbin.org/ip'
    # for i in range(1,11):
    #     #Get a proxy from the pool
    #     proxy = next(proxy_pool)
    #     print("Request #%d"%i)
    #     try:
    #         response = requests.get(url,proxies={"http": proxy, "https": proxy})
    #         print(response.json())
    #     except:
    #         #Most free proxies will often get connection errors. You will have retry the entire request using another proxy to work. 
    #         #We will just skip retries as its beyond the scope of this tutorial and we are only downloading a single url 
    #         print("Skipping. Connnection error")
            
    def parse(self, response):
        
        items = EmpireItem()
        newlist = []
        newlist2 = []
        newlist3 = []
        newlist4 = []

       
        ids = response.css('.listing-id a::text').extract()
        niche = response.css('#results-listing h5::text').extract()
        monetization = response.css('.monetization span::text').extract()[::2]
        price = response.css('.price span::text').extract()
        net = response.css('.monthly-net-profit span::text').extract()
        multiple = response.css('.multiple span::text').extract()

        def get_ids(id):
            for i in id:
                i = int(re.sub(r'[^\w]','',i))
                newlist.append(i)
            return newlist
        
        def get_price(p):
            for i in p:
                i = int(re.sub(r'[^\w]','',i))
                newlist2.append(i)
            return newlist2

        def get_net(n):
            for i in n:
                i = int(re.sub(r'[^\w]','',i))
                newlist3.append(i)
            return newlist3

        def get_multi(mul):
            for i in mul:
                i = int(re.sub(r'[^0-9]','',i))
                newlist4.append(i)
            return newlist4


        ids = get_ids(ids)
        price = get_price(price)
        net = get_net(net)
        multiple = get_multi(multiple)

        items['ids'] = ids
        items['niche'] = niche
        items['monetization'] = monetization
        items['price'] = price
        items['net'] = net
        items['multiple'] = multiple

        yield items

        asset_page = response.css('div.listing-item-row a::attr(href)').extract()

        for link in asset_page:
            yield scrapy.Request(
                url = link,
                callback= self.parse_asset_data
            )


    def parse_asset_data(self, response):
            
        items = EmpireItem()
        newlist = []
        newl = []
        newl2 = []
        newl3 = []
        newl4 = []
        
        ee = []
        e = []
        eee = []
        eeee = []

       
        
                
        
        

        
        ids = response.xpath('/html/body/div[2]/div/section[3]/div/div/div[1]/ul/li[1]/text()').extract()
        pricing_period = response.css('.sites-summary_left li:nth-child(5)::text').extract() 
        monthly_revenue = response.css('.sites-summary_left li:nth-child(3)::text').extract()
        hrs_worked_per_week = response.css('.grids-information:nth-child(9) .grids-information-left p::text').extract()
        platfrom = response.css('.grids-information-left p:nth-child(5)::text').extract()
        domain_type = response.css('.grids-information-left p:nth-child(4)::text').extract()
        year_created = response.css('.sites-summary_right p:nth-child(2)::text').extract()
        page_views = response.xpath('//*[@id="traffic-twelve"]').extract()
        unique_users= response.xpath('//*[@id="traffic-twelve"]').extract()

        
       
        def get_ids(id):
            for i in id:
                i = int(re.sub(r'[^\w]','',i))
                newlist.append(i)
            return newlist

        def pp_to_int(pp):
            for i in pp:
                i = int(i[:-8])
                newl.append(i)
            return newl

        def mr_to_int(mr):
            for i in mr:
                i = int(re.sub(r'[^\w]','',i))
                newl2.append(i)
            return newl2
        
        def hw_to_int(hw):
            for i in hw:
                i = int(re.sub('[^0-9]','',i))
                newl3.append(i)
            return newl3

        def yc_to_y(yc):
            for i in yc:
                i = re.sub('[^0-9]','',i)
                newl4.append(i)
            return newl4


        def get_page_views(page_view):
            for i in page_view:
                i = re.findall('[0-9]+', i)
                pvs = i[12:24]
                for pv in pvs:
                    pv = int(pv)
                    ee.append(pv)
                    agv_p = sum(ee)//12
                eee.append(agv_p)
            return eee

        def get_unique_users(u_u):
            for i in u_u:
                i = re.findall('[0-9]+', i)
                unique_usrs = i[24:36]
                for uu in unique_usrs:
                    uu = int(uu)
                    e.append(uu)
                    agv_uu = sum(e)//12
                eeee.append(agv_uu)
            return eeee


        ids = get_ids(ids)
        pricing_period = pp_to_int(pricing_period)
        monthly_revenue = mr_to_int(monthly_revenue)
        hrs_worked_per_week = hw_to_int(hrs_worked_per_week)
        year_created = yc_to_y(year_created)
        page_views = get_page_views(page_views)
        unique_users = get_unique_users(unique_users)

        items['ids'] = ids
        items['pricing_period'] = pricing_period
        items['monthly_revenue'] = monthly_revenue
        items['hrs_worked_per_week'] = hrs_worked_per_week
        items['platfrom'] = platfrom
        items['domain_type'] = domain_type
        items['year_created'] = year_created
        items['page_views'] = page_views
        items['unique_users'] = unique_users
        yield items

