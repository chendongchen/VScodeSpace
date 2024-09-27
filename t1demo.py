import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from PIL import Image
import os
import string 
import re
import ssl

image_count = 0
image_size = 100
pagesixe =100

#urlslcet = 'https://w2.xiuren.ee/4393.html'

# 使用ssl创建未验证的上下文，在url中传入上下文参数
context = ssl._create_unverified_context()
# 将context传入url函数的context参数中，比如
image_dir ="./imagedownload/"
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

# #访问指定网页
# webpage_url = urlslcet

# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# req = urllib.request.Request(url=webpage_url, headers=headers)

# webpage = urlopen(req,timeout=100)

# # page_content = webpage.read()
# # print(page_content)

# #解析网页内容
# suop = BeautifulSoup(webpage,"html.parser")
# image_tags = suop.findAll('img') 
# conter_image=0
# for imgtag in image_tags: 
#     if conter_image>4:
#         break
#     conter_image=conter_image+1
#     print(imgtag)
#     imgtag_link = imgtag['data-original']
#     imgtag_link = urllib.parse.quote(imgtag_link,safe=string.printable)
#     imgtag_link = urllib.request.Request(url=imgtag_link, headers=headers)

#     try:
#         imageload = urlopen(imgtag_link,timeout=1,context=context)
#         image = Image.open(imageload)
#         image_filename = image_dir + "image_%03d.png" %(image_count)
#         image.save(image_filename)
#         image_count = image_count + 1
#     except:
#         continue

#     if image_count > image_size:
#         break

# 使用ssl创建未验证的上下文，在url中传入上下文参数
context = ssl._create_unverified_context()
    # 将context传入url函数的context参数中，比如
image_dir ="./imagedownload/"
if not os.path.exists(image_dir):
         os.makedirs(image_dir)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

urlslcet = 'https://w2.xiuren.ee/4393.html'

original_url = "https://w2.xiuren.ee/"

for newpage in range(pagesixe):
    urlslcet = original_url + "%03d" %(16004-newpage)+".html"
    print(urlslcet)
    try:
        #访问指定网页
        webpage_url = urlslcet       
        req = urllib.request.Request(url=webpage_url, headers=headers)
        webpage = urlopen(req,timeout=100)
        #解析网页内容
        suop = BeautifulSoup(webpage,"html.parser")
        image_tags = suop.findAll('img') 
        conter_image=0
        for imgtag in image_tags: 
            if conter_image>4:
                break
            conter_image=conter_image+1
            print(imgtag)
            imgtag_link = imgtag['data-original']
            imgtag_link = urllib.parse.quote(imgtag_link,safe=string.printable)
            imgtag_link = urllib.request.Request(url=imgtag_link, headers=headers)

            try:
                imageload = urlopen(imgtag_link,timeout=1,context=context)
                image = Image.open(imageload)
                image_filename = image_dir + "image_%03d.png" %(image_count)
                image.save(image_filename)
                image_count = image_count + 1
            except:
                continue
    except:
        continue
    if image_count > image_size:
        break