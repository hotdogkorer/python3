# 네이버 지도 데이터 수집하기
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


import time
#import requests
#from bs4 import BeautifulSoup
import re
import csv

def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


#import os
##################################################
# 파이썬 내부 라이브러리 time을 사용합니다.
# time: 시간과 관련된 여러가지 기능을 포함합니다.
##################################################
driver =set_chrome_driver()

# # 구버전 네이버지도 접속
driver.get("https://map.naver.com/v5/")
driver.implicitly_wait(3)

try:
   element = WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.CLASS_NAME, "input_search"))
   ) #입력창이 뜰 때까지 대기
finally:
   pass

##################################################

# 검색창에 검색어 입력하기 // 검색창: input#search-input
#input_search1651051953713
#search_box = driver.find_element(By.CLASS_NAME,"input_search")
search_box =  driver.find_element(By.CSS_SELECTOR, "input#search-input")

#search_box = driver.find_element(By.ID, 'input_search') 
search_box.send_keys("치킨")
search_box.send_keys(Keys.ENTER) #검색창에 "치킨" 입력
search_btn =driver.find_element(By.CSS_SELECTOR, "button.spm")

time.sleep(7) #화면 표시 기다리기
frame = driver.find_element(By.CSS_SELECTOR, "iframe#searchIframe")

driver.switch_to.frame(frame)

time.sleep(3)
# 여기까지 iframe 전환


scroll_div = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]")
#검색 결과로 나타나는 scroll-bar 포함한 div 잡고
driver.execute_script("arguments[0].scrollBy(0,2000)", scroll_div)
time.sleep(2)
driver.execute_script("arguments[0].scrollBy(0,2000);", scroll_div)
time.sleep(2)
driver.execute_script("arguments[0].scrollBy(0,2000);", scroll_div)
time.sleep(2)
driver.execute_script("arguments[0].scrollBy(0,2000);", scroll_div)
time.sleep(2)
driver.execute_script("arguments[0].scrollBy(0,2000);", scroll_div)
time.sleep(2)
#여기까지 scroll
#맨 아래까지 내려서 해당 페이지의 내용이 다 표시되게 함

# csv 파일 생성d
file = open('stores.csv', mode='w', newline='')
writer = csv.writer(file)
writer.writerow(["place", "rate", "address", "info", "image", "phone"])
final_result = []
time.sleep(1)
# # 반복 시작

i = 2
while i<=10: #몇 페이지까지 크롤링할 것인지 지정
   stores_box = driver.find_element_by_xpath("/html/body/div[3]/div/div[2]/div[1]/ul")
   #stores = driver.find_elements_by_css_selector("li._3t81n._1l5Ut")
   stores = driver.find_elements_by_css_selector("div.lsnx")
   #해당 페이지에서 표시된 모든 가게 정보
   
   for store in stores: #한 페이지 내에서의 반복문. 순차적으로 가게 정보에 접근
       name = store.find_element_by_css_selector("span.OXiLu").text #가게 이름

       
       try:    
           rating = re.search('/span>(\d).', store.find_element_by_css_selector("span._2FqTn._1mRAM").get_attribute('innerHTML')).groups()[0]
       except:
           rating = '별점없음'
       time.sleep(3)
       # 평점 숫자 부분만 rating에 담음. 평점이 없는 경우가 있어 예외 처리
       try:
           img_src = re.search('url[(]"([\S]+)"', store.find_element_by_css_selector("div.cb7hz").get_attribute('style')).groups()[0]
       except:
           img_src = '이미지 없음'
          #역시 대표 이미지가 없는 경우가 있어 예외 처리
       click_name = store.find_element_by_css_selector("span._3Yilt")
       click_name.click() 
       # 가게 주소, 홈페이지 링크를 확인하려면 가게 이름을 클릭해 세부 정보를 띄워야 함.


       driver.switch_to.default_content()
       time.sleep(7)        
       ##오래 헤맸던 부분!! switch_to.default_content()로 전환해야 frame_in iframe을 제대로 잡을 수 있다. 
       
       frame_in = driver.find_element_by_xpath('/html/body/app/layout/div[3]/div[2]/shrinkable-layout/div/app-base/search-layout/div[2]/entry-layout/entry-place-bridge/div/nm-external-frame-bridge/nm-iframe/iframe')

       driver.switch_to.frame(frame_in) 
       # 가게 이름을 클릭하면 나오는 세부 정보 iframe으로 이동
       time.sleep(3)
       try:
           #address = store.find_element_by_css_selector("dd.addr").text
          address = re.search('서울\s(\w+)\s', driver.find_element_by_css_selector("span._2yqUQ").text).groups()[0]
       except:
           address = '주소없음'
          #주소 정보 확인
       try:
           link_url = driver.find_element_by_css_selector("a._1RUzg").text
       except:
           link_url = '링크없음'
          # 홈페이지 url 확인
   
       try:
            phone = store.find_element_by_css_selector("dd.tel").text
       except:
            phone = ''
       
       store_info = {
           'placetitle':name,
           'rate':rating,
           'address':address,
           'info':link_url,
           'phone':phone,
           'image':img_src
       }
       #크롤링한 정보들을 store_info에 담고
       print(name, rating, address, img_src, link_url, phone)
       print("*" * 50)
       final_result.append(store_info)
       # 출력해서 확인 후 final_result에 저장

       driver.switch_to.default_content()
       driver.switch_to.frame(frame)
       time.sleep(8)
       # 한 페이지 크롤링 끝
     
     # '2'페이지로 이동하는 버튼 클릭 후 i 1증가 
   next_button = driver.find_element_by_link_text(str(i))
   next_button.click()
   i = i+1
   time.sleep(8)
   
#while문이 종료되면 크롤링 종료

for result in final_result: #크롤링한 가게 정보에 순차적으로 접근 & csv 파일 작성
    row = []
    row.append(result['placetitle'])
    row.append(result['rate'])
    row.append(result['address'])
    row.append(result['info'])
    row.append(result['image'])
    row.append(result['phone'])
    writer.writerow(row)
    
print(final_result)

driver.close()



