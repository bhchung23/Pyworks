#중첩 for
"""
for i in range(1,6): #5행
    for j in range(1,6): #5열
        print("가",end='')
    print() #행 바꿈
print("------------")

for i in range(5): #5행
    for j in range(5): #5열
        print("가",end='')
    print() #행 바꿈
print("------------")

for i in range(5): #5행
    for j in range(5): #5열
        print("*",end='')
    print() #행 바꿈
print("------------")


#구구단 전체 출력
for i in range(2,10):
    for j in range(1,10):
        print(f"{i}x{j}={i*j}")
    print()
print("수고하셨습니다!!")

#삼각형으로 별 찍기
for i in range(1,6): #5행
    for j in range(1,i+1):
        print("*",end='')
    print() #행 바꿈
print("------------")
"""

height = 5

for i in range(1, height + 1):
    # 공백 출력
    for j in range(height - i):
        print(" ", end="")

    # 별 출력
    for j in range(i):
        print("*", end="")

    # 줄 바꾸기
    print()