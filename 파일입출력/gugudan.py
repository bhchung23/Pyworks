#파일에 구구단 쓰기
try:
    with open("output/gugudan.txt", "w", encoding='utf-8') as f:
        for i in range(1, 10):
            f.write(f"3x{i}={3*i}\n")
      
except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")




