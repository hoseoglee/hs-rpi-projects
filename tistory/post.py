import sys
import json
import requests
import argparse

blogName = sys.argv[0]
token = sys.argv[1]
filename = sys.argv[2]

f = open("./contents/"+filename,'r')
file_content="<pre>";
while True:
    line = f.readline()
    if not line: break
    file_content += line
f.close()
file_content +="</pre>"

print(file_content)
output ='json'
title = filename
content = file_content
visibility = 0

params = {'access_token': token, 'output':output, 'blogName': blogName,'title': title,'content': content,'visibility': visibility}
rd = requests.post('https://www.tistory.com/apis/post/write', params=params)
print(rd)

try:
    item = json.loads(rd.text)
    print(item)
except:
    print("Failed")
