#
from tkinter import *

#버튼 클릭시 "버튼을 눌렀습니다." 문구를 출력
def click():
    #print("버튼을 눌렀습니다.")
    result.config(text="버튼을 눌렀습니다.")

root=Tk()

#command에 호출된 함수의 괄호는 반드시 생략함
Button(root,text="확인",command=click).pack(pady=20)
result=Label(root,text="여기에 출력")
result.pack()
root.mainloop()
