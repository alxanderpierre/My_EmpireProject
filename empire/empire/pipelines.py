# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import mysql.connector
from scrapy.exceptions import DropItem
# import pass_ 

class DuplicatesPipeline:
    def __init__(self):
        self.seen = set()

    def process_item(self, item, spider):
        if item.values() in self.seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.seen.add(item.values())
            return item






class EmpirePipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()
    
    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'password.',
            database = 'MyEmpire'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""CREATE TABLE IF NOT EXISTS Empire_Flippers_tb( 
            ids int PRIMARY KEY,
            niche text,
            monetization text,
            price int,
            net int,
            multiple int)""")
        
        
        self.curr.execute(""" CREATE TABLE IF NOT EXISTS Empire_Flippers_asset_tb(
            ids int PRIMARY KEY,
            pricing_period int,
            monthly_revenue int,
            hrs_worked_per_week int,
            platfrom text,
            domain_type text,
            year_created text,
            page_views int,
            unique_users int)""")
     
        
    def process_item(self, item, spider):
        if "niche" in item:
            self.store_db(item)
        else:
            self.store_db2(item)
        
        return item
        
    

    def store_db(self, item):
        for j in range(len(item["ids"])):

            self.curr.execute("""insert into Empire_Flippers_tb values (%s, %s, %s, %s, %s, %s)""",(
                item['ids'][j],
                item['niche'][j], 
                item['monetization'][j],
                item['price'][j],
                item['net'][j], 
                item['multiple'][j]))
            
            self.conn.commit()



    def store_db2(self, item):
        for j in range(len(item["pricing_period"])):

            self.curr.execute("""insert into Empire_Flippers_asset_tb values (%s, %s, %s, %s, %s, %s, %s, %s, %s) """,(
                item['ids'][j],
                item['pricing_period'][j],
                item['monthly_revenue'][j],
                item['hrs_worked_per_week'][j],
                item['platfrom'][j],
                item['domain_type'][j],
                item['year_created'][j],
                item['page_views'][j],
                item['unique_users'][j])) 

            self.conn.commit()


    
    
    # def store_db(self, item):
    #     for i in range(len(item["ids"])):

    #         self.curr.execute("""insert into Empire_Flippers_tb values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",(
    #             item['ids'][i],
    #             item['niche'][i], 
    #             item['monetization'][i],
    #             item['price'][i],
    #             item['net'][i], 
    #             item['multiple'][i]))
    #             item['pricing_period'][i],
    #             item['hrs_worked_per_week'][i],
    #             item['platfrom'][i],
    #             item['domain_type'][i],
    #             item['year_created'][i])) 

    #         self.conn.commit()
    
    
    
    # def store_db2(self, item):
    #     self.curr.execute("""insert into Empire_Flippers_tb values (%s, %s, %s, %s, %s)""",(
                    
    #         item['pricing_period'],
    #         item['hrs_worked_per_week'],
    #         item['platfrom'],
    #         item['domain_type'],
    #         item['year_created'])) 

    #     self.conn.commit()



    #_____________________________

    # def create_table(self):
    #     self.curr.execute(""" drop table if exists Empire_Flippers_tb """ )
    #     self.curr.execute("""create table Empire_Flippers_tb( 
    #         ids int,
    #         niche text,
    #         monetization text,
    #         price int,
    #         net int,
    #         multiple int)""")

    #     self.curr.execute(""" drop table if exists Empire_Flippers_asset_tb """ )
    #     self.curr.execute("""create table Empire_Flippers_asset_tb( 
    #         ids int,
    #         pricing_period int,
    #         monthly_revenue int,
    #         hrs_worked_per_week int,
    #         platfrom text,
    #         domain_type text,
    #         year_created text,
    #         page_views int,
    #         unique_users int)""")
            
            
            


# self.curr.execute(""" INSERT INTO Empire_Flippers_tb (
        #     ids, 
        #     niche,
        #     monetization,
        #     price, 
        #     net, 
        #     multiple) VALUES (%s, %s, %s, %s, %s, %s)""", (item['ids'],
        #         item['niche'], 
        #         item['monetization'],
        #         item['price'],
        #         item['net'], 
        #         item['multiple']))
        # self.conn.commit()

        # self.curr.execute("""INSERT INTO Empire_Flippers_asset_tb (
        #     ids, 
        #     pricing_period, 
        #     monthly_revenue, 
        #     hrs_worked_per_week,
        #     platfrom, 
        #     domain_type,
        #     year_created, 
        #     page_views, 
        #     unique_users) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", (item['ids'],
        #         item['pricing_period'],
        #         item['monthly_revenue'],
        #         item['hrs_worked_per_week'],
        #         item['platfrom'],
        #         item['domain_type'],
        #         item['year_created'],
        #         item['page_views'],
        #         item['unique_users']))
        # self.conn.commit()