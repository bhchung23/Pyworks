#이차원 리스트: 리스트 내부에 리스트를 포함한 자료구조
a=[[1,2,3],[4,5,6]] #지도좌표, 게임에서 많이 사용
a=[
    [1,2,3],
    [4,5,6]
]
print(a[0]) #first row
print(a[1])

print(a[0][0]) #first row, first 행
print(a[0][1])

#for문 출력
for row in a:
    for x in row:
        print(x,end="")
    print()