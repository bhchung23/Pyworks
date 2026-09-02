import re
'''
# findall() 함수 : 찾은 문자열을 리스트로 반환
text="오늘은 2026-09-02 입니다. 내일은 2026-09-03 입니다."
reg_exp=r"\d{4}-\d{2}-\d{2}"

dates=re.findall(reg_exp, text)
print("날짜 목록:", dates) #날짜 목록: ['2026-09-02', '2026-09-03']
print(dates[0]) #2026-09-02

for date in dates:
    print(date)

# 마스킹(***) 처리하기
# sub() 함수 : 마스킹 처리할 때 쓰는 함수
pattern=r"\d{3}-\d{4}\d{4}"
text="내 전화번호는 010-1234-5678 입니다."
masked_text=re.sub(pattern,"xxx-xxxx-xxxx",text)
print(masked_text)
print(re.sub('\d','*','a1b2c3'))
'''

#주민등록번호 뒷자리 마스킹
import re

def mask_resident_number(input_str: str) -> str:
    # 1. 입력값에서 숫자만 추출 (하이픈, 공백 제거)
    cleaned = re.sub(r'[^0-9]', '', input_str)
    
    # 2. 13자리가 맞는지 확인
    if len(cleaned) != 13:
        return "올바른 주민등록번호 형식이 아닙니다. (총 13자리의 숫자가 필요합니다.)"
        
    # 3. 뒷자리 첫 번째 숫자(성별)만 남기고 마스킹 처리
    return f"{cleaned[:6]}-{cleaned[6]}******"

# 🚀 여기에서 사용자에게 직접 입력을 물어봅니다!
user_input = input("주민등록번호를 입력하세요 (예: 950101-1234567): ")

# 결과 출력
result = mask_resident_number(user_input)
print("마스킹 결과:", result)