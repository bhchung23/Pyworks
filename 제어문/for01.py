#for 반복문
#range(시작값, 종료값, 증감값)
print(range(5))
print(list(range(5)))
print(list(range(1,6)))

#1~5까지 출력
for i in range(1,6,1):
    print(i)


#1~5합계
total=0
for i in range(1,6,1):
    total= total+i
print('합계:',total)


#1~5합계
total=0
for i in [1,2,3,4,5]:
    total= total+i
print('합계:',total)