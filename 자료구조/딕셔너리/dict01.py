"""
#data 1개 저장하면 변수, ex num=10
#4명의 성적을 저장하면 LIST, ex [75,80,90,85], 대괄호 사용
#dictionary: (key)age (value)30, name Tom....
#            여러 개의 값을 저장하는 점은 list와 같으나 key-value 쌍으로 저장, 중괄호 {} 사용
student={
    "name":"한강", 
    "age":21, 
    "university":"한국대학교"}

print(student)
print(type(student))

#key만 알면 요소에 접근 가능, 요소에 접근할 때는 key로 검색
print(student["name"])
print(student["age"])


#리스트와 다른 점은 요소 조회(검색)할 때 함수도 사용 가능
#리스트와 차이점을 구분하면 좋음
print(student.get("university"))

#요소 추가
student["major"]="전자공학"
print(student)

#d요소 삭제-pop(key)
student.pop("major")

#요소수정: list와 같음
student["age"]=25
print(student)

student.keys()
print(student.keys())
print(student.values())

#for 사용해서 전체 출력
for key in student.keys():
    print(key)
    print(key,':', student[key])
"""

#실습 11-1 딕셔너리로 회원정보를 만든다.
