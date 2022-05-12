import requests
from bs4 import BeautifulSoup

#############################################
# 추가1

# daumnews.csv 파일을 쓰기(w) 모드로 열어줍니다.
f = open("daumnews.csv", "w")

# 데이터의 헤더 부분을 써줍니다.
f.write("제목,기사요약\n")
#############################################

for n in range(1, 4):


    raw = requests.get("https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page="+str(n)+"&q=코알라")
    html = BeautifulSoup(raw.text, 'html.parser')

    articles = html.select("div.wrap_cont")

    for ar in articles:
        title = ar.select_one("a.tit_main").text
        summary = ar.select_one("p.desc").text

        print(title)
        print(summary)
        # 기사별로 구분을 위해 구분선 삽입
        print("="*50)

        #############################################
        # 추가2

        # ,로 데이터가 구분되지 않도록 수집한 제목/기사요약에서 ,를 삭제해줍니다.
        title = title.replace(",", "")
        summary = summary.replace(",", "")

        # 수집한 제목/저자를 파일에 써줍니다.
        f.write(title + "," + summary + "\n")
        #############################################

#############################################
# 추가3

# naverebook.csv파일을 닫아줍니다.
f.close()
####################################