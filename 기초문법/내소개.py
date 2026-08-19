"""
#type

num=10
pi=3.14
language="python"
is_merried=False

print(type(num),type(pi),type(language),type(is_merried))
"""

#형 변환(type converesion)
a="10"
b=5

a=int(a) #int(문자): 문자를 정수로 변환하는 함수

print(a+b) #15

#연습
a="10"
b="5"
print(a+b) #105
print(a,b) #10 5

#str(숫자): 숫자를 문자로 변환하는 함수
age=26
print("나이:"+str(age)) #나이:26
age="26"
print("나이:"+age) #나이:26
print("나이:",age) #나이: 26

#연습문제

x="7"
y="3"

print(int(x)+int(y)) #10

"""
#십진수 -> 이진수 변환 함수 : bin(심진수)

print(bin(33)) #0b100001
print(bin(25497))
print(bin(65)) #0b1000001

#chr(코드값) : 아스키코드값을 문자로 변환
print(chr(65)) #A
print(chr(33)) #!

#문자를 코드값으로 변환
print(ord('A')) #65
print(ord('!')) #33
"""
