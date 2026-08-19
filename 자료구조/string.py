"""
#문자열-string
#인덱싱-한개씩 추출
s=['s','k','y'] #문자를 하나씩 담은 리스트
print(s,[0])

s="python"
print(s[0])

#슬라이싱-여러개 추출
print(s[0:2]) #py
print(s[:3]) #앞 0을 생략 pyt
print(s[2:]) #2번에서 끝까지 thon
print(s[:-1]) #pytho

#split(구분기호):문자열을 리스트로 만들어 줌
fruit='banana,grape,apple'
fruit_list=fruit.split(',') #['banana', 'grape', 'apple']
print(fruit_list[0]) #banana

#문자를 수정하는 replace()
msg="Hello World"
print(msg)

msg=msg.replace('World','Korea')
print(msg)
"""

#공백 제거하는 함수-strip()
msg2=" hi, jun"
msg2=msg2.strip()
print(msg2)

#section9 예제
data = "홍길동 / 010-1234-5678 / 서울"

# '/'를 기준으로 나누고, 앞뒤 공백 제거
name, phone, city = [item.strip() for item in data.split("/")]

print("이름:", name)
print("전화번호:", phone)
print("도시:", city)

#9-1 이메일 아이디 추출
em="user@naver.com"
em=em.split('@')
print('아이디:',em[0],'도메인:',em[1])

id=em[0]
domain=em[1]
print("ID:", id)
print("Domain:", domain)
      