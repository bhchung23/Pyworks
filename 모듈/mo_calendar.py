
#달력 모듈 사용
import calendar

#2026전체 달력
#calendar.prcal(2026)
#calendar.prmonth(2026,8)

#요일이름
print(calendar.day_name[6])
print(calendar.day_name[:])
day_of_week=calendar.weekday(2026,12,25)
print(day_of_week)
print(calendar.day_name[day_of_week])

