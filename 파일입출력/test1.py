#실습2-1 메모 저장하기

#쓰는 모드
f = open("memo.txt", "w", encoding="utf-8")
f.write("파이썬은 재미있다\n매일 조금씩\n꾸준히\n")
f.close()

#오류처리 try-except 를 해주면 참조하는 memo.txt 가 사라져도 다운되지 않고 오류메세지를 출력하고 종료됨


try:
#읽는 모드
    f = open("memo.txt", "r", encoding="utf-8")
    print(f.read())
    f.close()
except FileNotFoundError:
    print("파일이 없습니다.")

