#타자 연습게임
import random
import time

word=["python","programming","challenge","developer","algorithm"]
n=1 #문제 번호

print("[타자게임] 준비되면 엔터!")
input()

start_time=time.time()

while n<=5:
    print("문제",n)
    q=random.choice(word)
    print(q) #문제 출제

    you=input() #사용자 입력 창
    if you ==q:
        print("정답입니다.")
        n=n+1
    else:
        print("오답입니다. 다시 도전!")
end_time=time.time()

es=end_time-start_time

print(f"게임에 걸린시간: {es:.2f}초")

