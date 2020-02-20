#read: 
#list:
#post:python tistory.py -token 6197da19acb927f1e69c796a362f5b2e_fe0cf1eab7c2681215ecf134788a5579 -action post -blogname cognitive -filename /home/pi/contents/2020/\[done\]20200218_외부_앱_실행  -visibility 3
#modify:

import sys
import json
import requests
import argparse
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-action', help='action')
parser.add_argument('-blogname', help='blogname')
parser.add_argument('-token', help='token')
parser.add_argument('-filename', help='filename')
parser.add_argument('-visibility', help='visibility')
parser.add_argument('-postid', help='postid')
args = parser.parse_args()

action = args.action
blogName = args.blogname
token = args.token
filename = args.filename
visibility = args.visibility

output = 'json'

def main():
    if action=='post':
        post(blogName, token, filename, visibility)
    elif action=='modify':
        print("modify")
    elif action=='list':
        print("list")
    elif action=='read':
        print("read")
    else:
        print("action")

    #post(blogName, token, filename, visibility)
	

def list(page):
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

def read(postId):
    params = {'access_token': token, 'output': output, 'blogName': blogName,'postId': postId}
    rd = requests.get('https://www.tistory.com/apis/post/read', params=params)
    print(rd)
    
    try:
        item = json.loads(rd.text)
        print(item)
    except:
        traceback.print_exc()

def post(blogname, token, filename, visibility):
    f = open(filename,'r')
    file_content="<pre>"
    while True:
        line = f.readline()
        if not line: break
        file_content += line
    f.close()
    file_content +="</pre>"
    
    print(file_content)
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
		

def modify(page):
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

if __name__=="__main__":
    main()
