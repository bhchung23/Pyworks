#제곱수 계산하는 리턴 함수
def square(x):
    return x*x

value=square(4)
print(value)

#두수의 합을 계산하는 리턴 함수
def add(x,y):
    return x + y

value2=add(10,20)
print(value2)

#원 넓이 계산 하는 리턴 함스
def circle_area(r):
    return 3.14*r*r

c_area=circle_area(5)
print('원의 넓이:',c_area,'m2')

def add(a, b):
    return a + b

result = add(3, 5)
print(result)

def cal(a,b):
    return 2*(a+b)
result=cal(4,5)
print(f"사각형의 넓이:{result} m2 입니다.")