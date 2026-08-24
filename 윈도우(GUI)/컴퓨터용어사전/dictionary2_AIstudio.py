from tkinter import *

# [데이터] 사전 데이터 초기값 (딕셔너리 구조)
# 키(Key)는 용어, 값(Value)은 설명입니다.
dic = {
    "변수": "데이터를 저장하기 위한 공간으로, 이름과 값으로 구성됩니다.",
    "함수": "특정 작업을 수행하는 코드 블록으로, 재사용이 가능합니다.",
    "CPU": "컴퓨터의 두뇌에 해당하는 핵심 장치(중앙 처리 장치)입니다.",
    "RAM": "컴퓨터가 작업하는 동안 데이터를 일시적으로 저장하는 기억 장치입니다.",
    "알고리즘": "어떤 문제를 해결하기 위해 정해진 일련의 절차나 방법입니다."
}

# [기능 1] 용어 검색 함수
def search():
    # 입력창(entry)에 쓴 글자를 가져와서 word 변수에 저장 (공백 제거)
    word = entry.get().strip()
    
    # 딕셔너리에서 단어를 찾음 (없으면 '사전에 없는...' 메시지 반환)
    meaning = dic.get(word, "사전에 등록되지 않은 용어입니다.")
    
    # 결과창(output)을 깨끗이 비우고(1.0부터 끝까지) 뜻을 출력
    output.delete(1.0, END)
    output.insert(END, f"[{word}]\n{meaning}")

# [기능 2] 새 용어 추가 함수
def add_word():
    # 추가할 단어와 뜻을 입력창에서 가져오기
    new_word = entry_add_word.get().strip()
    new_meaning = entry_add_meaning.get().strip()
    
    # 만약 입력창 중 하나라도 비어있다면 경고 메시지 출력
    if new_word == "" or new_meaning == "":
        output.delete(1.0, END)
        output.insert(END, "[알림] 추가할 단어와 뜻을 모두 입력해주세요!")
        return # 함수를 여기서 종료

    # 딕셔너리에 새로운 데이터 추가 (사전에 등록)
    dic[new_word] = new_meaning
    
    # 입력이 끝났으므로 입력칸을 비워줌
    entry_add_word.delete(0, END)
    entry_add_meaning.delete(0, END)
    
    # 결과창에 성공 메시지 출력
    output.delete(1.0, END)
    output.insert(END, f"✅ '{new_word}' 용어가 사전에 성공적으로 추가되었습니다!")

# --- GUI 화면 만들기 시작 ---

# 메인 창 생성
window = Tk()
window.title("나만의 컴퓨터 용어 사전")
window.geometry("500x500") # 창 크기 설정

# 1. 검색 영역
Label(window, text="🔎 검색할 용어를 입력하세요", font="돋움 11 bold").grid(row=0, column=0, padx=10, pady=10, sticky=W)
entry = Entry(window, width=35)
entry.grid(row=1, column=0, padx=10, pady=5)
# 엔터키를 눌러도 검색이 되게 하려면 아래 문장을 추가할 수 있습니다.
entry.bind("<Return>", lambda event: search())

btn_search = Button(window, text="검색하기", width=10, command=search, bg="skyblue")
btn_search.grid(row=1, column=1, padx=5, pady=5)

# 구분선 역할을 할 빈 라벨
Label(window, text="").grid(row=2, column=0)

# 2. 용어 추가 영역
Label(window, text="✨ 새로운 용어 추가하기", font="돋움 11 bold", fg="blue").grid(row=3, column=0, padx=10, pady=10, sticky=W)

Label(window, text="단어 입력:").grid(row=4, column=0, padx=10, sticky=W)
entry_add_word = Entry(window, width=35)
entry_add_word.grid(row=5, column=0, padx=10, pady=5)

Label(window, text="뜻 설명 입력:").grid(row=6, column=0, padx=10, sticky=W)
entry_add_meaning = Entry(window, width=50)
entry_add_meaning.grid(row=7, column=0, columnspan=2, padx=10, pady=5)

btn_add = Button(window, text="사전 추가", width=10, command=add_word, bg="lightgreen")
btn_add.grid(row=8, column=0, padx=10, pady=10, sticky=W)

# 3. 결과 출력 영역
Label(window, text="🗒 결과 및 알림", font="돋움 11 bold").grid(row=9, column=0, padx=10, pady=10, sticky=W)
output = Text(window, width=65, height=8, background="lightgray")
output.grid(row=10, column=0, columnspan=2, padx=10, pady=5)

# 창이 닫히지 않도록 유지
window.mainloop()