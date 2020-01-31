#python modify.py cognitive 0df016421981e1c012344d65277116b8_c31f27d8897f37a8e1ce2c6d2ea49035 1

import sys
import json
import requests
import argparse

blogName = sys.argv[1]
token = sys.argv[2]
page = sys.argv[3]

print("blogName:"+blogName)
print("token:"+token)

output ='json'

params = {'access_token': token, 'output':output, 'blogName': blogName,'page': page}
rd = requests.get('https://www.tistory.com/apis/post/list', params=params)
print(rd)

try:
    item = json.loads(rd.text)
    posts = item['tistory']['item']['posts']
    print(posts)
    print(len(posts))
except:
    print("Failed")
