
#사용자 정의 함수
#함수 정의 및 호출

def greet():
    print('안녕하세요!')

def greet_n(name):
    print(f"{name}님 안녕하세요!")

greet()
greet_n('성희')


#1-1 연습문제 인사함수 만들기
def info(name,age):
    print(f"안녕하세요! {name}님은 {age}살 입니다.")

info('정보현',26)
info('김대원',33)