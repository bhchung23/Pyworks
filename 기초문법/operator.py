"""
#산술 연산자
n1=7 #(=: 대입연산자)
n2=2
print(n1+n2,n1-n2,n1*n2) #9 5 14
print(n1/n2, n1//n2, n1%n2, n1**n2) #3.5 3 1 49




#연습문제: 몫과 나머지 구하기
#선언
bread=30
person=4

#계산
몫=bread//person
나머지=bread%person

#출력
print("한 사람 몫:",bread//person, "개") #7, 몫
print("남는 빵:",bread%person, "개") #2, 나머지

#f 스트링 함수 사용법
print(f"한 사람 몫:{bread//person}개") #일반 문장쓰듯, 변수만 중괄호 안에




#복합대입 연산자
count=10
count=count+2
print(count) #12

count=count-2
print(count) #10

count-=2
print(count) #8

count*=2
print(count) #16

count/=2
print(count) #8.0, 나눗셈은 결과가 항상 실수로 출력




#비교 연산자
a=3
b=4

print(a>b) #False
print(a<b) #True
print(a==b) #False
print(a!=b) #True


#논리 연산자
a=3
b=4
result=(a<b) and (a==b)
print(result) #False

result=(a<b) or (a==b)
print(result) #True

result=not(a!=b)
print(result) #False
"""
