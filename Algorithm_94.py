import re

import re

prefix= "gifs_"

img_lst = []

with open("keys/abc.txt" ,'r') as f:
    for i in f:
        if re.findall("GET",i,re.IGNORECASE):
            img_with_200 = re.findall("([a-zA-Z-0-9]*.gif HTTP/1.0' 200)", i, re.IGNORECASE)
            for j in img_with_200:
                imgs = j.split()
                img = imgs[0]
                code = imgs[-1]
                if code == "200" and img not in img_lst:
                    img_lst.append(img)
                    print(img)

for i in img_lst:
    print(i)