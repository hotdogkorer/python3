import requests # http 요청
import os # mkdir 명령을 위함
from bs4 import BeautifulSoup # html문서 파싱
from selenium import webdriver # 각종 브라우저를 제어하는 웹 드라이버
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.support import expected_conditions as EC 


def set_chrome_driver():
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver


driver =set_chrome_driver()

#river = webdriver.Chrome(web_driver_path) // web_driver_path 는 chromeDriver 파일의 경로

driver.get('https://www.instagram.com/') # 파싱을 하고싶은 홈페이지 경로

soup = BeautifulSoup(driver.page_source)

imgs = soup.findAll('img')
instagram_id="marob078"

os.mkdir('./' + instagram_id)

for img in imgs:
    response = requests.get(img['src'])
    filename = img['src'].split('/')[-1]
    extention = response.headers['Content-Type'].split('/')[-1]
    with open('./'+instagram_id+'/'+filename + '.' + extention, 'wb') as f:
        f.write(response.content)

driver.close()
