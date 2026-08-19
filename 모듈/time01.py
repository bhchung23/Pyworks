#
import time
print(time.time()) # 유닉스시스템이 시작된 1970년 1월 1일 자정부터 지금까지 흐른 시간을 초로 환산 

#일로 환산
days=round(time.time()/(24*60*60)) #라운드 이용하여 정수로 정리
print(days) #20684

years=round(days/365)
print(years) #57

#시간대기 지연 함수
#print("3초 후에 메시지가 출력됩니다.")
#time.sleep(3)
#print("3초가 지났습니다.")

#0.5초 간격으로 1~10까지 출력
for i in range(1,11):
    print(i)
    time.sleep(0.5)
