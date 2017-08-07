# -*- coding: utf8 -*-
import requests
from GetUserAgents_from_web import LinkedinCookies
import redis
from GetUserAgents_from_web import ua_list_now
import random
db=redis.StrictRedis(host='localhost',port='6379',db = 0,decode_responses=True,password='try_123as_pass')

proxies  = {
  'http': 'http://' + [db.get(key) for key in db.keys()][0]
}
headers={'User-Agent':random.choice(ua_list_now)

}
print([db.get(key) for key in db.keys()][0])
url='http://cn.linkedin.com/in/%E5%8D%BF%E9%9C%96-%E7%89%9B-b1649797'
r=requests.get(url,proxies=proxies,allow_redirects=True)
r.encoding='UTF-8'
print(r.status_code)
#print(r.text)
