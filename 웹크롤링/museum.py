#
from bs4 import BeautifulSoup

import requests

#1. 국립중앙박물관 사이트 ->관람 정보->관람 안내 

# 2. Rrl 가져오기
url = "https://www.museum.go.kr/MUSEUM/contents/M0101000000.do"
response=requests.get(url)
#print(response)
#print(response.text)


# 3.beautifulSoup:소스 전체 가져오기
soup=BeautifulSoup(response.text, 'html.parser')
#print(soup)
'''
# 4.관람시간만 추출
first_ul=soup.select_one('ul.display-content')
print(first_ul)
#print(first_ul.text) 함수를 이용해서 추출
print(first_ul.get_text())
'''
# 5.관람정보 전체 항목 추출하기
contents=soup.select('ul.display-content-area > li > ul')
#print(contents)
print(contents[1].get_text()) #휴관일