# import packages




from tqdm.auto import tqdm
from tqdm import tqdm_notebook

from selenium import webdriver
from bs4 import BeautifulSoup
import copy
import time
import random
import json
import pandas as pd 

# set selenium


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


chrome_options = set_chrome_driver()



google_url = 'https://www.google.com/'
twitter_url = 'https://twitter.com/MH_Rise_JP/status/'

keywords = {'【新・映像見聞録】':'신・영상견문록', '【狩猟の導き書サブレ】':'사냥의 인도서', 
           '開発イラスト':'개발 일러스트', 'ディレクターの鈴木です。':'디렉터 스즈키입니다.', 
           '開発背景スタッフおすすめスポット':'개발 배경 직원 추천 명소', '【担当者コメント】':'담당자 코멘트'}

driver.implicitly_wait(3)

result_df = pd.DataFrame(columns=['keyword','title','URL', 'text', 'translated'])

for keyword in keywords:
  driver.get(google_url)
  time.sleep(random.randrange(1,3))
  search_next = True
  
  # give text
  search_word = '\"'+keyword+'\" '+'site:'+twitter_url
  search_word_src = driver.find_element_by_name('q')
  print(f'[DEBUG] 검색어 : {search_word}')
  search_word_src.send_keys(search_word)
  search_word_src.submit()

  while search_next != None:
    if search_next == True:
      pass
    else:
      new_url = google_url + search_next['href']
      print(f'[DEBUG] new_url : {new_url}')
      driver.get(new_url)

    # wait 
    time.sleep(random.randrange(1,3))

    # get html & parsing
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # get result
    ## format 1
    search_results = soup.findAll("div", {"class":"dXiKIc"})
    for i in search_results:
      link_url = i.find('a')['href'].lower()
      # for duplicate check 
      if '?' in link_url:
        link_url = link_url.split('?')[0]

      texts = i.find("div", {"class":"Uroaid"}).text
      title = texts.split(keyword[-1])[0]+keyword[-1]
      print(texts)
      print(link_url)
      result_df = result_df.append({'keyword':keywords[keyword],'title':title,'URL':link_url, 'text':texts, 'translated':'tmp'}, ignore_index=True)
      print()
    
    ## format 2
    if len(search_results) == 0:
      search_results = soup.findAll("div", {"class":"jtfYYd"})
      for i in search_results:
        tmp_link = i.find("div", {"class":"yuRUbf"})
        link_url = tmp_link.find('a')['href'].lower()
        # for duplicate check 
        if '?' in link_url:
          link_url = link_url.split('?')[0]

        texts = i.find("div", {"class":"VwiC3b.yXK7lf.MUxGbd.yDYNvb.lyLwlc.lEBKkf"})
        # exception handling
        if texts == None:
          title = keyword
          texts = keyword
        else:
          title = texts.split(keyword[-1])[0]+keyword[-1]

        print(texts)
        print(link_url)
        result_df = result_df.append({'keyword':keywords[keyword],'title':title,'URL':link_url, 'text':texts, 'translated':'tmp'}, ignore_index=True)
        print()
    
    # if next page exists
    search_next = soup.find(id='pnnext')

# print(results_dict)
result_df = result_df.sort_values(by=['title'])
result_df
