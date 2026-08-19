"""
#내장함수=파이썬에서 제공되는 함수
a=[1,3,5,1] #list는 중복되어도 됨
print(sum(a))
print(len(a))
print(min(a))

#반올림 round
b=352.567
print(round(b))
print(round(b,1)) #소수 첫째자리까지 반올림
print(round(b,2)) #소수 둘째자리까지 반올림
print(round(b,-1)) #1의 자리에서 반올림
print(round(b,-2)) #10의 자리에서 반올림

#절대값-abs(x)
print(abs(8))
print(abs(-8))
"""

#직접만든 절대값 함수
def my_abs(x):
    if x<0:
        return x*-1 # = -x
    else:
        return x
print(my_abs(-8))
