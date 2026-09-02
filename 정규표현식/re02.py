import re #내장된 모듈이라 별도 설치하지 않음,. 외부 모듈이면 pip...해서 설치해야..
'''
#휴대폰 번호 검사
#fullmatch()함수: 전체문자가 일치하는지 확인하는 함수 vs match: 첫글자가 일치하는지 확인하는 함수
phone="010-12-56789"
if re.fullmatch('010-\d{3,4}-\d{4}', phone):
    print("올바른 휴대폰 번호입니다.")
else:
    print("잘 못 된 휴대폰 번호입니다. 다시 입력하세요.")
'''
# 이메일, @ 전후 표현식 확인, .은 \로 표현, +는 특수기호가 아니라 전체를 검토한다는 의미, email이 제일 복잡하다
email="hong%.!!@naver.com"
re_exp="[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}"
if re.fullmatch(re_exp, email):
    print("올바른 이메일 형식입니다.")
else:
    print("잘못된 이메일 형식입니다.")

