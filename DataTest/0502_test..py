import requests
from bs4 import BeautifulSoup

#############################################
# 추가1

# 쓰기버전(w)으로 navernews.csv파일을 연다.
f = open("navernews.csv", "w")
# 데이터의 헤더부분을 입력한다.
f.write("제목, 언론사\n")

#############################################

page = 1
for page in range(1, 100, 10):
    raw = requests.get("https://search.daum.net/search?w=news&nil_search=btn&DA=NTB&enc=utf8&cluster=y&cluster_page="+str(page)+"&q=코알라")
    html = BeautifulSoup(raw.text, 'html.parser')

    # 컨테이너: ul.type01 > li
    # 기사제목: a._sp_each_title
    # 언론사: span._sp_each_source

    #1. 컨테이너 수집
    articles = articles = html.select("div.wrap_cont")

    #2. 기사 데이터 수집

    for ar in articles:
        title = ar.select_one("a.tit_main").text
        source = ar.select_one("span.f_nb").text

        print(title, source)
        #3. 반복하기
        

        #############################################
        # 추가2

        # 제목(title)과 언론사(source)에 ,가 포함되어있는 경우
        # 데이터가 구분될 수 있으므로 ,를 삭제해줍니다.
        title = title.replace(",", "")
        source = source.replace(",", "")

        # 제목(title)과 언론사(source)를 ,로 구분하여 써줍니다.
        f.write(title + ',' + source + '\n')

        #############################################


#############################################
# 추가3

# navernews.csv 파일을 닫아줍니다.
f.close()

#############################################