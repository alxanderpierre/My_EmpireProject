# def parse_links(self, response):
#         next_page = response.css('div.listing-item-row a::attr(href)').extract() 
#         for link in next_page:
#             yield scrapy.Request(url = link, callback = self.parse_next_page)
    
#     def parse_next_page(self, response):
        
#         items = EmpireItem()
#         pricing_period = response.css('.sites-summary_left li:nth-child(5)::text').extract()
       
#         items['pricing_period'] = pricing_period
        
#         yield items
        

#     def parse_assets(self, response):
        
#         items = EmpireItem()
#         newlist = []
#         newlist2 = []
#         newlist3 = []
#         newlist4 = []

#         for data in response.css('.marketplace-bottom'):
#             ids = data.css('.listing-id a::text').extract()
#             niche = data.css('#results-listing h5::text').extract()
#             monetization = data.css('.monetization span::text').extract()[::2]
#             price = data.css('.price span::text').extract()
#             net = data.css('.monthly-net-profit span::text').extract()
#             multiple = data.css('.multiple span::text').extract()

#             def get_ids(id):
#                 for i in ids:
#                     i = int(re.sub(r'[^\w]','',i))
#                     newlist.append(i)
#                 return newlist
            
#             def get_price(prices):
#                 for i in price:
#                     i = int(re.sub(r'[^\w]','',i))
#                     newlist2.append(i)
#                 return newlist2

#             def get_net(nets):
#                 for i in net:
#                     i = int(re.sub(r'[^\w]','',i))
#                     newlist3.append(i)
#                 return newlist3

#             def get_multi(multiples):
#                 for i in multiple:
#                     i = int(re.sub(r'[^0-9]','',i))
#                     newlist4.append(i)
#                 return newlist4


#             ids = get_ids(ids)
#             price = get_price(price)
#             net = get_net(net)
#             multiple = get_multi(multiple)

#             items['ids'] = ids
#             items['niche'] = niche
#             items['monetization'] = monetization
#             items['price'] = price
#             items['net'] = net
#             items['multiple'] = multiple

#             yield items

   

#         # for link in response.css('.marketplace-bottom'):
#         #     asset_page = link.css('div.listing-item-row a::attr(href)').extract()
#         #     yield scrapy.Request(url = asset_page[0], callback= self.parse_asset_data)

#     # def kdfjdljf(self):
#     #     asset_page = 'https://empireflippers.com/listing/48035/'
#     #     yield scrapy.Request(url = asset_page, callback= self.parse_asset_data)





#     def parse_asset_data(self, response):
#         items = EmpireItem()
#         for data in response.css('.grids-information:nth-child(11) .grids-information-left , .grids-information:nth-child(9) .grids-information-left , .sites-summary_left , .sites-summary_left p , .sites-summary_right'):
#             pricing_period = data.css('.sites-summary_left li:nth-child(5)::text').extract() 
#             monthly_revenue = data.css('.sites-summary_left li:nth-child(3)::text').extract()
#             hrs_worked_per_week = data.css('.grids-information:nth-child(9) .grids-information-left p::text').extract()
#             platfrom = data.css('.grids-information-left p:nth-child(5)::text').extract()
#             domain_type = data.css('.grids-information-left p:nth-child(4)::text').extract()
#             year_created = data.css('.sites-summary_right p:nth-child(2)::text').extract()
            
#             items['pricing_period'] = pricing_period
#             items['monthly_revenue'] = monthly_revenue
#             items['hrs_worked_per_week'] = hrs_worked_per_week
#             items['platfrom'] = platfrom
#             items['domain_type'] = domain_type
#             items['year_created'] = year_created

#             yield items
#         # yield scrapy.Request(url = "https://empireflippers.com/marketplace/", callback= self.parse)

        




#     #         if asset_page:
#     #         items = EmpireItem()

#     #         pricing_period = int(response.css('.sites-summary_left li:nth-child(5)::text').get()[:-8])  
#     #         monthly_revenue = int(re.sub(r'[^\w]','', response.css('.sites-summary_left li:nth-child(3)::text').get()))
#     #         hrs_worked_per_week = int(re.sub('[^0-9]','',response.css('.grids-information:nth-child(9) .grids-information-left p::text').get())) 
#     #         platfrom = response.css('.grids-information-left p:nth-child(5)::text').get()
#     #         domain_type = response.css('.grids-information-left p:nth-child(4)::text').get()
#     #         year_created = re.sub('[^0-9]','',response.css('.sites-summary_right p:nth-child(2)::text').get())
            
#     #         items['pricing_period'] = pricing_period
#     #         items['monthly_revenue'] = monthly_revenue
#     #         items['hrs_worked_per_week'] = hrs_worked_per_week
#     #         items['platfrom'] = platfrom
#     #         items['domain_type'] = domain_type
#     #         items['year_created'] = year_created

#     #         yield items
            
        
#     #     if asset_page:
#     #         url = data.url.join(asset_page[0].extract()) 
#     #         yield scrapy.Request(url, callback=self.parse_asset_data_on_next_page)
        
       
       
    





       
 
#         # for next_page in response.css('div.listing-item-row a::attr(href)'):
#         #     if next_page is not None: 
#         #         next_page = response.urljoin(next_page)
#         #         yield scrapy.Request(next_page, callback= self.parse, dont_filter=True)

#         # for pricing_period in response.css('div.listing-item-row a::attr(href)'):
#         #     yield {'pricing_period': int(pricing_period.get()[:-8]) }

           

           


#         #  def link_parse(self, response):
#         # links = response.css('div.listing-item-row a::attr(href)').extract()
#         # for links in links:
#         #     url = link.get()
