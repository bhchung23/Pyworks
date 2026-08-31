import requests

# 1. 파이썬 사이트 방문



# 2. URL 가져오기
url = "https://www.python.org/"
response = requests.get(url)
print(response) #<Response [200]> 정상이라는 의미
print(response.text) # HTML 내용 출력

# 3.HTML 다루기 - BeautifulSoup 설치
