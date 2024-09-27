import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
from PIL import Image
import os
import string 
import re
import ssl

image_count = 0
image_size = 1000
urlslcet = 'https://w2.xiuren.ee/'

# 使用ssl创建未验证的上下文，在url中传入上下文参数
context = ssl._create_unverified_context()
# 将context传入url函数的context参数中，比如
image_dir ="./imagedownload/"
if not os.path.exists(image_dir):
    os.makedirs(image_dir)

#访问指定网页
webpage_url = urlslcet

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
req = urllib.request.Request(url=webpage_url, headers=headers)

webpage = urlopen(req,timeout=100)
suop = BeautifulSoup(webpage,"html.parser")
image_tags_url = suop.findAll('a',class_ = "img") 

for imgtag in image_tags_url: 
    #生成新网页
    print(webpage_url+imgtag['href'])
    nowwebpage_url = webpage_url+imgtag['href']

    nowreq = urllib.request.Request(url=nowwebpage_url, headers=headers)
    nowwebpage = urlopen(nowreq,timeout=100)
    nowsuop = BeautifulSoup(nowwebpage,"html.parser")
    #print(nowsuop)
    image_tags = suop.findAll(name = 'img')
    #print(image_tags)
    step=0
    for imgtag in image_tags: 
        try:
           # print(imgtag['data-original'])
            imgtag_link = imgtag['data-original']
            imgtag_link = urllib.parse.quote(imgtag_link,safe=string.printable)
            imgtag_link = urllib.request.Request(url=imgtag_link, headers=headers)
            imageload = urlopen(imgtag_link,timeout=1,context=context)           
            image = Image.open(imageload)
            image_filename = image_dir + "image_%03d.png" %(image_count)
            image.save(image_filename)
            image_count = image_count + 1      
        except:
           continue
        if image_count > image_size:
           break 
        if step>image_size :
            break
        step = step+1

#<img alt="[XiuRen秀人网] No.9064 杨晨晨Yome 黑丝美腿" class="lazy" src="https://ooo111.ka123.sbs/pic/2024_09_23/XiuRen秀人网No9064杨晨晨Yome黑丝美腿/3.jpg" data-original="https://ooo111.ka123.sbs/pic/2024_09_23/XiuRen秀人网No9064杨晨晨Yome黑丝美腿/3.jpg" style="display: block;">
#page_content = webpage.read()
#print(page_content)

# #解析网页内容
# suop = BeautifulSoup(webpage,"html.parser")
# image_tags = suop.findAll('img') 

# for imgtag in image_tags: 
#     print(imgtag)
# {"alt":"[XiuRen秀人网] No.4644 豆瓣酱 丝袜美腿"}
#<img alt="[XiuRen秀人网] No.4644 豆瓣酱 丝袜美腿" class="lazy" src="https://ooo111.ka123.sbs/pic/2022_05_19/XiuRen秀人网No4644豆瓣酱丝袜美腿/u2wmfvtufvl.jpg" data-original="https://ooo111.ka123.sbs/pic/2022_05_19/XiuRen秀人网No4644豆瓣酱丝袜美腿/u2wmfvtufvl.jpg" style="display: block;">
#print(image_tags)

# image_dir ="./imagedownload/"
# if not os.path.exists(image_dir):
#     os.makedirs(image_dir)



# image_count = 0
# for imgtag in image_tags: 
#     imgtag_link = imgtag['data-original']
#     imgtag_link = urllib.parse.quote(imgtag_link,safe=string.printable)
#     imgtag_link = urllib.request.Request(url=imgtag_link, headers=headers)
#     imageload = urlopen(imgtag_link,timeout=1,context=context)

#     print(imgtag)
#     print(imgtag_link)

    
    # image = Image.open(imageload)

    # image_filename = image_dir + "image_%03d.png" %(image_count)
    # image.save(image_filename)
    # image_count = image_count + 1
    # if image_count > 100:
    #     break

