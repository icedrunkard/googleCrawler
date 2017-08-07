# -*- coding: utf-8 -*-
from urllib.parse import quote_plus
import requests
from .qText import query



def genHeaders(name,school):
    H=[]

    headers={
    ':authority':'vip.kuaimen.bid',
    ':method':'GET',
    ':path':'',
    ':scheme':'https',
    'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'accept-encoding':'gzip, deflate, sdch, br',
    'accept-language':'zh-CN,zh;q=0.8',
    'authorization':'Basic aWNlZDpydW5r',
    'cookie':'UM_distinctid=15daa2678875e7-02da00b929ef17-314b7b5f-1fa400-15daa26788870a; CNZZDATA1260920938=357490342-1501793144-%7C1501793144',
    'referer':'https://vip.kuaimen.bid/',
    'upgrade-insecure-requests':'1',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2372.400 QQBrowser/9.5.10548.400',
    }

    for i in query(name,school):
        q='/search?'+quote_plus(i)+'&filter=0'
        #print(q)
        headers[':path']=q
        H.append(headers)


    return H
genHeaders('sdjhg','中南大学')
