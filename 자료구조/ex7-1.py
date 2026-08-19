#실습7-1(교안)

#점수 리스트 [88, 92, 79, 95, 60]의 합계·평균·최고점·최저점을 출력하세요.
score = [88, 92, 79, 95, 60]

print(len(score))
print(sum(score))

#average=sum/len
count=len(score)
total=sum(score)
average=total/count
print(average)
print(sum(score)/len(score))

print("최고점:",max(score))
print("최저점:",min(score))

#전체 점수 출력
for i in score:
    print(i)


#평균이상 출력
for i in score:
    if i>=average:
         print(i)