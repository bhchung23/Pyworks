
import random #random.py를 가져옴
"""
#한번만 랜덤으로 하고 싶을 때-seed 설정
#random.seed(42) #시드 설정
#print(random.random()) #0.0~1.0 사이의 난수 발생

#1~10 사이의 정수 난수 발생
print(random.randint(1, 10))

#동전던지기
#0이면 앞면, 1이면 뒷면
coin = random.randint(0, 1)
if coin == 0:
    print("앞면")
else:
    print("뒷면")  

#문자열에서 랜덤으로 선택: choice() 함수 사용
fruits = ["apple", "banana", "cherry", "date"]
print(random.choice(fruits))

#랜덤하게 섞기: shuffle() 함수 사용
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)

#로또 번호 생성기(1~45 사이의 6개의 번호를 랜덤으로 선택)
  #방법1
lotto=[] #일단 빈 리스트 생성

n = random.randint(1,45)
print(n) #랜덤으로 뽑은 번호 출력


#6번 반복
while len(lotto)<6: #6개를 뽑을 동안은 계속 작동
    n = random.randint(1,45) #난수 발생
    if n not in lotto: #번호 중복 방지 코드
       lotto.append(n) #리스트에 추가
print(lotto)

  #방법2 :파이선에서 sample 함수를 이미 만들어 놨음
print(random.sample(range(1,46),6))
"""
