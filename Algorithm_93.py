import re

string = "burger.letters.com - - [01/Jul/1995:00:00:12 -0400] 'GET /shuttle/countdown/video/livevideo.GIF HTTP/1.0' 200 0"
prefix= "gifs_"
filename = input()
img_lst=[]
with open(filename, 'r') as f:
    content = f.read()
    img_with_200 = re.findall("([a-zA-Z-0-9]*.gif HTTP/1.0' 200)", content, re.IGNORECASE)
    for ls in img_with_200:
        img_200 = ls.split()
        img = img_200[0]
        code = img_200[-1]
        if code == "200" and img not in img_lst:
            img_lst.append(img)
for i in img_lst:
    print(i)
with open(prefix + filename, 'w')as w:
    for i in img_lst:
        w.write(i + "\r\n")

print(re.findall("([a-zA-Z-0-9]*.gif HTTP/1.0' 200)",string,re.IGNORECASE))

