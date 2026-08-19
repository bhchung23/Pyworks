
#숫자 리스트의 연산
score=[80,70,90,75]

#갯수 세는 함수 len
print(len(score))

#더하는 함수
total=score[0]+score[1]+score[2]+score[3]
print(total)
print(score[0]+score[1])
"""
#더하는 sum 함수
total=sum(score)
"""
#평균 =합계/갯수
count=len(score)
average=total/count
print(average)

#최대값:max(list)
max_val=max(score)
print('최고점수:',max_val)

#최소값:min(list)
min_val=min(score)
print('최저점수:',min_val)

#ex. 7-1(교안), 평균이상 점수만 출력 할 것!
for s in score:
    if s >= average:
        print(s)
    