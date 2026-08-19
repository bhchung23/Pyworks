"""
# while break 문
#1부터 5까지 출력
n=1
while True:
    if n>5:
        break
    print(n)
    n=n+1


#1~5까지 합계구하기
n=1
total=0
while True:
    if n>5:
        break
    total = total + n
    n=n+1
print(total)
"""
#종료가 나올때까지 반복
while True:
    msg=input('입력(exit를 입력하면 끝남): ')
    if msg=='exit':
       print('대화를 종료합니다.')
       break
    print('입력된 말:',msg)

