#python read.py cognitive 243c7aef9ecc15803a5b45733b20d373_1cb80a9267f1b2def2210ce5d6b15426 88

import sys
import traceback
import json
import requests
import argparse

blogName = sys.argv[1]
token = sys.argv[2]
postId = sys.argv[3]

print("blogName:"+blogName)
print("token:"+token)

output ='json'

params = {'access_token': token, 'output': output, 'blogName': blogName,'postId': postId}
rd = requests.get('https://www.tistory.com/apis/post/read', params=params)
print(rd)
try:
    item = json.loads(rd.text)
    print(item)
except:
    traceback.print_exc()

