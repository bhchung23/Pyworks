
#반복문-while
#1~5까지 출력(시작값 1 종료값 5, 증가값 1)

n=1
while n <= 10: #True 면 계속 출력
    print(n)
    n=n+1
print('반복을 종료합니다.')


n=1
while n <= 5: #True 면 계속 출력
    print(n)
    n=n+1
print('반복을 종료합니다.')


#1부터 5까지 합계 구하기(1+2+3+4+5)
n=1 #시작점
total=0 #시작점
while n <=5:
    total += n #total = total + n
    n += 1 #n = n+1
    print(total)
print('계산이 완료되었습니다.','총합은',total,'입니다.')

#while 보다 더 많이 쓰는 일반적인 구문: while true~
