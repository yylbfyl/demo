import requests
import os,time
import re
from bs4 import  BeautifulSoup
root = "D:\\Project\\temp3\\"
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3018.3 Safari/537.36'}
baseurl = "https://www.676tu.com/tupian/68484.html"
try:
    r = requests.get(baseurl, headers=headers)
    demo = r.text
    soup = BeautifulSoup(demo, "html.parser")
except:
    print(soup.prettify())


'''
for tag in soup.find_all(True):
    print(tag.name)
'''

for link in soup.find_all(re.compile('img')):
    picurl = link.get('data-original')
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    path = root + now + picurl.split('/')[-1]
    #    path = root + picurl.split('/')[-2] + picurl.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            pic = requests.get(picurl,headers = headers)
            with open(path, 'wb') as f:
                f.write(pic.content)
                f.close()
                print(picurl + "file saved")
                time.sleep(0.001)
        else:
            print("file existed")
    except:
        print("failed")


#print(soup.prettify())