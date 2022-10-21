# # -*- coding: utf-8 -*-
# import http.client, urllib
# import json      #引入json库
# conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
# params = urllib.parse.urlencode({'key':'762fd0fc00239d3d9acc63ffe55e77e1'})
# headers = {'Content-type':'application/x-www-form-urlencoded'}
# conn.request('POST','/lzmy/index',params,headers)
# res = conn.getresponse()
# data = res.read()
# data = json.loads(data)  #转换成字典
# print (data["newslist"][0]["saying"])

# -*- coding: utf-8 -*-
from hmac import new
import http.client, urllib
import json      #引入json库
conn = http.client.HTTPSConnection('api.tianapi.com')  #接口域名
params = urllib.parse.urlencode({'key':'762fd0fc00239d3d9acc63ffe55e77e1'})
headers = {'Content-type':'application/x-www-form-urlencoded'}
conn.request('POST','/zaoan/index',params,headers)
res = conn.getresponse()
data = res.read()
data = json.loads(data)  #转换成字典
print(data["newslist"][0]["content"])