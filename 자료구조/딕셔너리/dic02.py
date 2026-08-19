"""
#딕셔너리 자료구조
dic = {} #빈 딕셔너리 선언

dic[1]='a'
dic[2]='b'
dic[3]='c'

print(dic) #{1: 'a', 2: 'b', 3: 'c'}
print(type(dic)) #<class 'dict'>
"""

#딕셔너리 예제
carts={1:"양말",2:"여름바지",3:"손수건"}
print(carts) #{1: '양말', 2: '여름바지', 3: '손수건'}

#2번키의 값을 알고 싶을 때
carts[2]
print(carts[2]) #여름바지

#데이터를 수정할 때: key로 검색
carts[3]="반팔티"
print(carts)

#for를 이용하여 전체 조회
for key in carts.keys():
    print(carts[key]) #양말 여름바지 반팔티
    print(key,":", carts[key]) #1 : 양말 2 : 여름바지 3 : 반팔티