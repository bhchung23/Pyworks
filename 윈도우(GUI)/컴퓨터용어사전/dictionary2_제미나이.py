"""
#컴퓨터 용어사전 윈도우버전(GUI)
from tkinter import *

# 딕셔너리 자료 생성
dic = {
    "변수": "데이터를 저장하기 위한 공간으로, 이름과 값으로 구성됩니다. ",
    "함수": "특정 작업을 수행하는 코드 블록으로, 재사용이 가능하며 입력과 출력을 가질 수 있습니다. ",
    "CPU": "중앙 처리 장치(Central Processing Unit)의 약자로, 컴퓨터의 두뇌에 해당하는 핵심 부품입니다. ",
    "RAM": "임의 접근 메모리(Random Access Memory)의 약자로, 컴퓨터가 작업을 수행하는 동안 데이터를 일시적으로 저장하는 메모리입니다. ",
}

# 검색 함수 정의
def search():
    word = entry.get().strip().upper() # 입력 상자에서 단어 가져오기(공백제거)
    meaning = dic.get(word, "사전에 없는 용어입니다.") #없을시 안내문
    output.delete(1.0, END) #이전 결과 지우기
    output.insert(END, word + " : " + meaning) #결과 출력

# 메인 윈도우 생성
window = Tk()
window.title("컴퓨터 용어 사전")

# 검색어 입력 레이블과 엔트리(입력상자- 한줄)
Label(window, text="용어를 입력하세요:") \
.grid(row=0, column=0, sticky=W, padx=10, pady=5)

entry = Entry(window, width=30)
entry.grid(row=1, column=0, sticky=W, padx=10, pady=5)

# 검색 버튼
Button(window, text="검색", command=search) \
.grid(row=2, column=0, sticky=W, padx=10, pady=5)

# 결과 출력 텍스트(여러줄)
output = Text(window, width=50, height=10)
output.grid(row=3, column=0, sticky=W, padx=10, pady=5)

window.mainloop()
"""

#컴퓨터 용어사전 윈도우버전(GUI)
from tkinter import *

# 딕셔너리 자료 생성 (용어 사전 데이터 기본값)
dic = {
    "변수": "데이터를 저장하기 위한 공간으로, 이름과 값으로 구성됩니다. ",
    "함수": "특정 작업을 수행하는 코드 블록으로, 재사용이 가능하며 입력과 출력을 가질 수 있습니다. ",
    "CPU": "중앙 처리 장치(Central Processing Unit)의 약자로, 컴퓨터의 두뇌에 해당하는 핵심 부품입니다. ",
    "RAM": "임의 접근 메모리(Random Access Memory)의 약자로, 컴퓨터가 작업을 수행하는 동안 데이터를 일시적으로 저장하는 메모리입니다. ",
}

# [기능 1] 검색 함수 정의
def search():
    word = entry.get().strip().upper()  # 입력 상자에서 단어 가져오기(공백제거, 대문자변환)
    meaning = dic.get(word, "사전에 없는 용어입니다.")  # 없으면 안내문 출력
    output.delete(1.0, END)  # 이전 결과 창 비우기
    output.insert(END, word + " : " + meaning)  # 결과창에 단어와 뜻 출력

# [기능 2] 새 용어 추가 함수 정의
def add_word():
    new_word = entry_add_word.get().strip().upper()  # 추가할 단어 가져오기 (공백제거, 대문자변환)
    new_meaning = entry_add_meaning.get().strip()   # 추가할 뜻 설명 가져오기 (공백제거)
    
    # 예외 처리: 단어나 뜻이 비어있는 경우 안내문 출력
    if new_word == "" or new_meaning == "":
        output.delete(1.0, END)
        output.insert(END, "[알림] 추가할 단어와 뜻 설명을 모두 입력해주세요!")
        return # 함수 종료
        
    # 사전(딕셔너리) 데이터에 새로 입력받은 단어와 뜻 추가하기
    dic[new_word] = new_meaning
    
    # 추가 완료 후 단어/뜻 입력창 깨끗하게 비우기
    entry_add_word.delete(0, END)
    entry_add_meaning.delete(0, END)
    
    # 결과창에 성공 메시지 보여주기
    output.delete(1.0, END)
    output.insert(END, f"★ [{new_word}] 용어가 사전에 새로 등록되었습니다! 검색창에서 검색해 보세요.")

# 메인 윈도우 생성
window = Tk()
window.title("컴퓨터 용어 사전 (용어 추가 기능 포함)")

# --- 1구역: 용어 검색 창 ---
Label(window, text="🔎 검색할 용어를 입력하세요:").grid(row=0, column=0, sticky=W, padx=10, pady=5)
entry = Entry(window, width=30)
entry.grid(row=1, column=0, sticky=W, padx=10, pady=5)

# 검색 버튼 (누르면 search 함수가 실행됩니다)
Button(window, text="검색", command=search, width=10).grid(row=1, column=1, sticky=W, padx=10, pady=5)

# --- 2구역: 새 용어 추가 창 ---
Label(window, text="✨ 사전에 없는 새 용어 추가하기:").grid(row=2, column=0, sticky=W, padx=10, pady=20)

# 추가할 단어 입력 레이블과 칸
Label(window, text="- 추가할 단어:").grid(row=3, column=0, sticky=W, padx=10)
entry_add_word = Entry(window, width=30)
entry_add_word.grid(row=4, column=0, sticky=W, padx=10, pady=5)

# 추가할 뜻 설명 입력 레이블과 칸
Label(window, text="- 뜻 설명:").grid(row=5, column=0, sticky=W, padx=10)
entry_add_meaning = Entry(window, width=55)
entry_add_meaning.grid(row=6, column=0, columnspan=2, sticky=W, padx=10, pady=5)

# 추가하기 버튼 (누르면 add_word 함수가 실행됩니다)
Button(window, text="추가하기", command=add_word, width=10, bg="lightgreen").grid(row=7, column=0, sticky=W, padx=10, pady=5)

# --- 3구역: 알림 및 결과 출력 화면 ---
Label(window, text="🗒 [결과 화면]").grid(row=8, column=0, sticky=W, padx=10, pady=10)
output = Text(window, width=60, height=8)
output.grid(row=9, column=0, columnspan=2, sticky=W, padx=10, pady=5)

# 윈도우 실행 유지
window.mainloop()

