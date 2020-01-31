import sys
import json
import requests
import argparse

blogName = sys.argv[1]
token = sys.argv[2]
filename = sys.argv[3]
visibility = sys.argv[4]

print("blogName:"+blogName)
print("token:"+token)
print("filename:"+filename)

def post(blogName, token, filename, visibility):
    f = open("/home/pi/contents/"+filename,'r')
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

    params = {'access_token': token, 'output':output, 'blogName': blogName,'title': title,'content': content,'visibility': visibility}
    rd = requests.post('https://www.tistory.com/apis/post/write', params=params)
    print(rd)

    try:
        item = json.loads(rd.text)
        print(item)
    except:
        print("Failed")

post(blogName, token, filename, visibility)
