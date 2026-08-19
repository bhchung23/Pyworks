#list 여러 개의 data를 저장하는 자료 구조
#변수는 1개의 Data를 저장하는 공간(변경가능)
#cart1='포도'
#cart2='커피'
#print(cart1,',',cart2)

#list 특징 (1)순서가 있다. 0번 부터 시작 (2)중복 가능 (3)요소 업데이트 가능, (4)요소 삭제 가능, (5)특정 요소 있는지 검색
carts = ['포도','커피','바나나','딸기','달걀']
#print(carts)
#print(type(carts))

#특정 요소를 조회하거나 접근하려면
print(carts[1],carts[4])
print(carts[-1],carts[4])
print(carts[-1],carts[-3])

#(3)
carts[2]='토마토'
print(carts[2])
print(carts)

#(4)
del carts[1]
print(carts)

#(5)
print('달걀' in carts)
print('양파' in carts)
print('양파' not in carts)

#전체 요소 출력
for cart in carts:
    print(cart)