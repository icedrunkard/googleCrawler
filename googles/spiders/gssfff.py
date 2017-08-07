# -*- coding: utf-8 -*-
from scrapy import FormRequest,Request,Spider
import re
from bs4 import BeautifulSoup as bs
from urllib.parse import urlencode
from googles.items import GooglesItem
#from googles.headersText import genHeaders      #根据人名/学校名，产生headers列表，4个元素
from googles.qText import query 
from googles.name_to_redis import NameToRedis                #含ToRedis(),
from googles.settings import COLLECTION_NAME,MONGO_DATABASE,MONGO_HOST
#from googles.get_google_links import base_q_ch,base_q_en
import pymongo
import redis
import random
#from xpinyin import Pinyin
from googles.GetUserAgents_from_web import ua_list_now
import time

client = pymongo.MongoClient(MONGO_HOST)
db = client[MONGO_DATABASE]#变更学校
col=db[COLLECTION_NAME+'_papers']#变更学院
db2=client['schools']
col2=db2['dpts_985']

NAME=[]
"""
db0存代理ip，db1存该学院的学生姓名，db2存学生linkedin链接特征码，
"""
db_name=redis.StrictRedis(host='localhost',port='6379',db = 1,decode_responses=True,password='try_123as_pass')
db_c=redis.StrictRedis(host='localhost',port='6379',db = 2,decode_responses=True,password='try_123as_pass')
db_s=redis.StrictRedis(host='localhost',port='6379',db = 15,password='try_123as_pass')

class GsSpider(Spider):    
    name = 'gss0'
    allowed_domains = ['*']
    base_url='http://{}/search?'#谷歌镜像

    def start_requests(self):
        headersGoogle={
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36',
                    }

        NameToRedis()
        db_c.flushdb()#清除原有特征码

        school=col2.find_one({'short':MONGO_DATABASE})['university']
        for name in db_name.keys():
            for q in query(name,school):
                #print(db_s.hget('adsl','adsl1').decode('utf-8'))
                if 'adsl' in db_s.keys():            
                    #qurl=self.base_url.format(db_s.hget('adsl','adsl1').decode('utf-8'))
                    qurl=self.base_url.format('localhost')
                else:
                    time.sleep(5)
                    #qurl=self.base_url.format(db_s.hget('adsl','adsl1').decode('utf-8'))
                    qurl=self.base_url.format('localhost')
                payload={'q':q,'filter':'0'}
                print(q)
                
                yield FormRequest(qurl,
                                  method='GET',
                                  headers=headersGoogle,
                                  #cookies=cookies,
                                  dont_filter=True,
                                  formdata=payload
                              )
            
    def parse(self,response):
        pass
