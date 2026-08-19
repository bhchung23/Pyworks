"""
#변수의 유효범위
def click_a():
    x=0 #함수 안에 있으므로 지역변수(local), 한바퀴 돌아도 값이 초기화 되는 경우
    x=x+1
    print("x=",x)

click_a()
click_a()

#실행값이 유지 되는 변수
#global 변수
quantity=2
def get_price():
    price=1000*quantity #price local 변수
    print(f"{quantity}개에 {price}입니다.")

get_price()
print(quantity)
print(price) #오류남, 로컬 변수는 한 번 계산하고 사라짐

"""
x=0 #전역변수(gobal)
def click_b():
    global x #글로벌 붙이면 지역변수 위치지만 전역변수화 한다.
    x+=1
    print("X=",x)

click_b()
click_b()

