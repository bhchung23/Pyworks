#컴퓨터 용어사전(콘솔버전)

print("♠컴퓨터 용어사전♠")

#딕셔너리 자료구조 사용
dic={
    "변수":"테이터를 저장하는 메모리 공간",
    "함수":"특정 작업을 수행하는 코드의 집합",
    "CPU":"컴퓨터의 중앙처리장치",
    "RAM":"컴퓨터의 주기억장치"
}
while True:
    word=input("검색할 단어를 입력하세요(종료는 exit 입력):")

# while ture문은 항상 빠져나올 수 있는 종료조건을 입력
    if word =="exit":
        print("프로그램을 종료합니다.")
        break
    elif word in dic:
        #print(f"{dic[word]}") 아래와 같은 결과
        print(f"{dic.get(word)}")
    else:
        print("사전에 없는 단어입니다.")
