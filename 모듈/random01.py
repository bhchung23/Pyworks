import random #random.py를 가져옴
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