#
from tkinter import *

def click():
    name=entry.get() #입력상자에 입력된 문자를 가져옴
    #result.config(text="안녕하세요, "+ name +"님!")
    result.config(text=f"안녕하세요, {name}님!")

root=Tk() #클래스 첫글자는 대문자
root.title("인사하기 프로그램")
root.geometry("240x150")

#1줄 입력상자 만들기(객체변수를 받아서 가져옴)
entry=Entry(root) #클래스 첫글자는 대문자
entry.pack(pady=10)

#버튼(기능만 있으므로 변수로 받을 필요 없음)
Button(root, text="인사하기",command=click).pack() #클래스 첫글자는 대문자

#라벨(객체변수를 받아서 가져옴)
result=Label(root, text="") #클래스 첫글자는 대문자
result.pack(pady=10)

root.mainloop()