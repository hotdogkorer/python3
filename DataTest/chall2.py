import requests
from bs4 import BeautifulSoup

url = 'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

movieInfoList = soup.find('ol', attrs={'class':'movie_list'}).find_all('li')

for movieInfo in movieInfoList:
    movieRank = movieInfo.find('span', attrs={'class':f'img_number'}).get_text()
    movieImg = movieInfo.find('img')['src']
    movieTitle = movieInfo.find('a', attrs={'class':'tit_main'}).get_text().replace(':', '')
    imgSrc = requests.get(movieImg, headers=headers)
    with open(f'{movieRank}-{movieTitle}.jfif', 'wb') as imgFile:
	    imgFile.write(imgSrc.content)
    