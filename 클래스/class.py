#자료형: 변수, 리스트, 딕셔너리
#함수

#객체지향언어(OOP) : C > C++ > Java > Python
#클래스: 자료형중 제일 크다
#속성(변수)과 매서드(함수)를 가진 코드
#선언방법: class 클래스 이름:
#             생성자(함수)-변수 포함
#             매서드(함수)

#어제 배운 모듈(파이썬 파일)은 변수, 리스트, 함수, 클래스 모두 가지고 있다.



#클래스-사물(객체)의 속성과 기능을 코드로 만든 것
class Car:
    #생성자(constructor)
    def __init__(self,color,model,wheel):
        self.color=color
        self.model=model
        self.wheel=wheel

    def drive(self):
        print(f"{self.color}{self.model}가 달립니다.")
#여기까지는 설계도 이므로 아무런 작동을 하지 않는다.

#객체(인스턴스) 생성
car=Car("검정색","Sonata",4)
print(car) #<__main__.Car object at 0x00000251B5564440>
car.drive() #매서드 호출, "검정색Sonata가 달립니다."
