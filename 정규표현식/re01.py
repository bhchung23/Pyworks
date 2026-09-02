#
import re #정규표현식 모듈 불러오기

# match(표현식, 문자열), [] 첫번째 문자 일치를 확인, +를 해주면 전체 텍스트를 다 찾음
#m=re.match('[a-z]+','korea')
#print(m) #<re.Match object; span=(0, 1), match='k'>
#print(m.group()) #k, korea

# search() 문자열 위치 어디든 반환, \d=숫자라는 의미, +는 전체 라는 의미
s=re.search('\d','abc123de')
print(s) #<re.Match object; span=(3, 6), match='123'>