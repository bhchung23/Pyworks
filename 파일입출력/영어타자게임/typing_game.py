#타자 연습게임
import random
import time

#외부의 word.txt를 읽어와서 단어를 리스트에 저장
try:
    with open("output/word.txt","r",encoding='utf-8') as f:
        word=[line.strip() for line in f]
except FileNotFoundError:
        print("파일을 열 수 없습니다.") 
n=1 #문제 번호

print("[타자게임] 준비되면 엔터!")
input()

start_time=time.time()

while n<=10:
    print("문제",n)
    q=random.choice(word) #위 8행 word 리스트에서 랜덤으로 단어를 선택
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

