
#리스트
fruit="grape" #문자열 변수
print(fruit)

fruits=["grape","apple","banana"] #리스트
print(fruits)

#리스트는 순서가 있음 앞에서부터:0,1,2, 뒤에서부터:-1,-2,-3
print(fruits[1])
print(fruits[-2])

#리스트에 요소 추가하는 함수: append() -> 맨 뒤에 추가, 다만 1개만 입력가능, 모자라면 extend([])
fruits.append("kiwi")
print(fruits) #['grape', 'apple', 'banana', 'kiwi']

#요소 삭제: remove()
fruits.remove("banana")
print(fruits) #['grape', 'apple', 'kiwi']

#요소 수정(업데이트)
fruits[1]='banana'
print(fruits) #['grape', 'banana', 'kiwi']

#전체 요소(목록) 출력
for f in fruits:
    print(f,end=' ') #grape banana kiwi('' 중간에 공백을 넣으면 답도 띄어서 출력한다.)

#아무것도 담겨있지 않은 상태에서 숫자를 담는 list
num=[] #텅 빈 리스트
num.append(10)
print(num) #[10]

num.append(20)
print(num) #[10, 20]

num.append(30)
print(num) #[10, 20, 30]

num.remove(20)
print(num) #[10, 30]

#실습문제 8-1(장바구니 관리)
cart=[]
cart.append("우유")
cart.append("빵")
cart.append("계란")
cart.remove("빵")
cart.pop() #맨 뒤 요소 삭제
print(cart)

#커피와 과자를 추가하는 매서드
cart.extend(["coffee","과자"]) #변수로 list(대괄호) 입력
print(cart)

#--전체 요소 출력
for i in cart:
    print(i)