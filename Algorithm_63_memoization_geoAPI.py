from pyproj import Proj,transform
import requests


url = "https://sgisapi.kostat.go.kr/OpenAPI3/addr/geocode.json"
req = "?accessToken={}&address={}"

file = open('keys/key','r')
key = file.readline()

#UTM-K
proj_UTMK = Proj(init='epsg:5178')
#WGS1984
proj_WGS84 = Proj(init='epsg:4326')

#memoization technique!
hash2 = {}
def getXY(df):
    if df.주소 in hash2:
        return hash2[df.주소]
    else:
        addr= df.주소
        url_req = requests.get(url+req.format(key,addr)).json()
        x1,y1 = url_req['result']['resultdata'][0]['x'], url_req['result']['resultdata'][0]['y']
        #UTM-K -> WGS84 만들기
        x2,y2 = transform(proj_UTMK,proj_WGS84,x1,y1)
        hash2[df.주소] = f"{x2},{y2}"
        return hash2[df.주소]



