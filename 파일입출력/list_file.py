#파일에 리스트 저장
fruits=["포도","딸기","참외","수박","토마토"]
with open("output/fruits.txt","w",encoding='utf-8') as f:
    for fruit in fruits:
        f.write(fruit + " ")

#파일 읽기
with open("output/fruits.txt","r",encoding='utf-8') as f:
    print(f.read())
