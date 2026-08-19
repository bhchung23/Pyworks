"""
#함수 예제
def msg():
    return "Good Luck!"
message=msg()
print(message)

#사각형 넓이 함수: w*h
def area(w,h):
    #pass #음 생각하자
    return w*h
area=area(4,3)
print("사각형의 면적:",area)

#삼각형 넓이 : w*h*0.5

def triangle():
    return w*h/2

tri_area = triangle(4,3)
print("삼각형의 넓이:",tri_area)
"""
#구구단 5단

def gugudan(dan):
    for i in range(1,10):
        print(f"{dan}*{i}={dan*1}")