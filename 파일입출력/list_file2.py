#파일에 리스트 저장
fruits=["포도","딸기","참외","수박","토마토"]
with open("output/fruits.txt","w",encoding='utf-8') as f:
    for fruit in fruits:
        f.write(fruit + "\n")

#파일 읽기-읽을 때 리스트에 담기
with open("output/fruits.txt","r",encoding='utf-8') as f:
    """lines=[]
    for line in f:
        lines.append(line.strip()) #strip은 공백 제거"""
    lines=[line.strip() for line in f] #리스트 내포
print(lines)