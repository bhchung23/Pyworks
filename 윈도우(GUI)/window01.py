#tkinter 라이브러리(모듈보다 좀 더 큰 개념)를 불러오기
from tkinter import * #*은 모든 함수나 클래스를 의미

#객체 생성- 창 만들기_pack 방식(기본적으로 가운데 정렬)
root=Tk()
root.title("첫 윈도우 만들기")
root.geometry("300x100") #창 크기(너비, 높이)

#배치, 위치도 필요- pack() 이나 grid로 만든다

#lbel:글자 출력하는 클래스
Label(root,text="안녕하세요").pack(pady=10)
Button(root,text="확인").pack()

root.mainloop()