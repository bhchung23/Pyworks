
#변수
from datetime import datetime
now=datetime.now()
print(now)

count=4 #변수선언과 초기화(값을 기억)
print("학생수:",count) #학생수: 4

#list의 선언과 초기화
scores=[90,75,80,40] #list
x=[1,2,3]
y=[4,5,6]

print(x+y) #two list를 합칠 뿐이지 숫자를 더하는 건 아님 [1, 2, 3, 4, 5, 6]
print(x*2) #x 라는 list를 한 번 더 연결 [1, 2, 3, 1, 2, 3]

#1~5까지 list에 저장
number=[] #빈 리스트를 변수로 저장
#number.append(1)
#number.append(2)... for문으로 바꾸는 건 아래처럼
for i in range(1,6):
    number.append(i)
print(number) #[1, 2, 3, 4, 5]

#한 발 더 들어가면...data분석에서는 이게 너무 길어:list의 내포
number2=[i for i in range(1,6)] #앞에 i는 저장하는 위치
print("number2=",number2) #number2= [1, 2, 3, 4, 5]

#1~10 중 짝수만 저장
evens=[]
for i in range(1,11):
    if i%2==0:
        evens.append(i)
print(evens) #[2, 4, 6, 8, 10]

evens2=[i for i in range(1,11) if i%2==0]
print("evens2:",evens2) #evens2: [2, 4, 6, 8, 10]

