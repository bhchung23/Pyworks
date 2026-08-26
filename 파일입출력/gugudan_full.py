#
try:
    with open("gugudan.txt", "w", encoding="utf-8") as f:
        for i in range(2,10):
            for j in range(1,10):
                f.write(f"{i}X{j}={i*j}\n")
except FileNotFoundError:
    print("File not found.")

#파일 읽기
try:
    with open("gugudan.txt","r",encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found.")
