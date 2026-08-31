# pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup

# 1. 서울시청 사이트 >메뉴글자 수집


# 2. url 가져오기
url = "https://www.seoul.go.kr/main/index.jsp"
response = requests.get(url)
#print(response.text)

# 3. beautifulsoup으로 html 다루기
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title) # title 태그 가져오기
print(soup.title.text)

# 4. 메뉴 글자 수집(여러개를 가져오기 위해 select 사용, 1개 가져올때는 select_one 사용)
all_li=soup.select('div.m_service ul li')
#print(all_li)
print(all_li[0])

# 5. 전체 목록 가져오기
for li in all_li:
    print(li.text.strip())
