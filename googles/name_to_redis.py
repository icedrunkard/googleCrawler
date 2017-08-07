# -*- coding: utf8 -*-
import pymongo
import redis
from .settings import COLLECTION_NAME,MONGO_DATABASE,MONGO_HOST
client = pymongo.MongoClient(MONGO_HOST)
db = client[MONGO_DATABASE]#变更学校
col=db[COLLECTION_NAME+'_papers']#变更学院


def GetPaperAuthors():
    s=set()
    for i in col.find():
        for a in i['author']:
            s.add(a['name'])
    return s




def NameToRedis():#变更host
    db=redis.StrictRedis(host='localhost',#host='localhost'host='123.206.177.39'
                         port='6379',
                         db =1,
                         decode_responses=True,
                         password='try_123as_pass')#password='try_123as_pass'
    s=GetPaperAuthors()
    db.flushdb()
    for i in s:
        
        db.set(i,i)
    print('NAME TO REDIS OK')


