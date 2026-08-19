"""
#if (else) 조건문

age=14

#조건식 결과값이 True 일 때만 실행, 콜론 다음줄은 4칸이 자동으로 들여쓰기
if age>=15: 
    print("입장 가능합니다.")
else: #age<15
    print("입장 할 수 없습니다.")



#if (elif) (else) 다중조건문
signal="노랑"

if signal=="빨강":
    print("STOP")
elif signal=="노랑":
    print("주의하세요")
else:
    print("건너가세요")
"""

#if (elif) (else) 다중조건문
signal=input("색상을 입력하세요(빨강, 파랑, 노랑): ")

if signal=="빨강":
    print("STOP")
elif signal=="노랑":
    print("주의하세요")
elif signal=="파랑":
    print("건너가세요")
else:
    print("색상이 없습니다.")
