# 파이션 html 파싱

import requests
from bs4 import BeautifulSoup  as bs

#raw = requests.get("https://tv.naver.com/r")
raw = requests.get("https://tgd.kr/s/ddraming")

soup = bs(raw.text, "html.parser")

elements = soup.select('div.esg-entry-content a > span')

print(elements)
#print(raw.text)cls

#html  = BeautifulSoup(raw.text ,"html.parser" )
#print(html)
#clips = html.select("div.div")
#print(html)
#title = clips[0].select_one("div.span")
#print(title) # 파싱한것중에서 html tag 제거 

