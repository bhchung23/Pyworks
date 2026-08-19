"""
#매개변수(괄호안에 있는 거)
def my_abs(x):
    if x<=0:
        return -x
    else:
        return x

print(my_abs(-2))

#매개변수가 list 일 때
def func(a):
    a2=[]
    for i in a:
        a2.append(i)
    return a2

arr=[1,2,3,4]
print(func(arr))


#기본 매개변수
def take_bus(fare):
    print(f"버스요금은 {fare}원 입니다.")

take_bus(1500)

#변수가 여러개 일 때, 기본 매개변수는 뒷쪽에 만들고, 일반 매개변수는 앞에 위치시킨다.
#함수를 호출할 때 기본 매개변수는 생략 가능

def take_bus(passenger,fare=1500): #위와 같은 결과
    print(f"버스요금은 {fare}원이고, 승객수는 {passenger}명 입니다.")

#take_bus(5) #일반버스
take_bus(6,1900) #프리미엄버스
"""

