#학생 성적표 프로그램
student_list=[
    {"name":"이대한","kor":95,"eng":80,"math":80},
    {"name":"박민국","kor":80,"eng":75,"math":75},
    {"name":"오상식","kor":90,"eng":85,"math":90}
]

#학생리스트 출력
print("첫 번째 요소 검색:",student_list[0])
print("첫 번째 요소 검색:",student_list[0]["name"])


print("***학생 성적표***")
print("이름\t국어\t영어\t수학\t평균") #\:탭 키
for student in student_list:
    name=student["name"]
    kor=student["kor"]
    eng=student["eng"]
    math=student["math"]
    toatl = kor + eng + math #총점
    average=toatl/3  #평균 구하기: 총점 /과목수
    average=toatl / (len(student)-1) #student의 숫자-1
    print(f"{name}\t{kor}\t{eng}\t{math}\t{average:.2f}") #소숫점 둘째 자리: ".2f"

#2차원 list

