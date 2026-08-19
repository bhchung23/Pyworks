
#안녕하세요 3번출력 하시오

#while 문
n=1
while n<=3:
    print("안녕하세요")
    n=n+1
#for 문
for n in range(3): #range(0,3)=0,1,2
    print("안녕하세요")

#for를 이용한 구구단: 일반형태 3*1=3
dan=int(input("단을 입력하세요: "))
for i in range(1,10,1):
    #print(dan,"x",i,"=",dan*i)
    print(f"{dan}x{i}={dan*i}")