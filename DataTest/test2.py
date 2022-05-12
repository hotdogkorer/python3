# 파이션 html 크롤링 예제cls
import requests
import re
from bs4 import BeautifulSoup as bs

for n in range(1,2) :
    page = requests.get("https://tgd.kr/s/ddraming/page/"+str(n))
    soup = bs(page.text, "html.parser")

    txt = str(soup.select(".article-list-row.has-category > div > div.list-title a"))
    txt=re.sub('<.+?>', '', txt, 0).strip() # html tag 제거 )
    alist = list()
    alist.append(txt)
    idx=1
    print(str(n), "페이지")
    print(len(alist))
    for idx,item in enumerate(iterable=alist, start=1):
        print( str(idx)+'번째 '+ item)
      
   


  
       








