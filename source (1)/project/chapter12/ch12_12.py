import time

gt = time.gmtime()
print('time.gmtime() : ', gt)  # GMT 시간

# 상수를 이용한 GMT 시간 출력
print('tm_year : ', gt.tm_year)  # 년
print('tm_mon : ', gt.tm_mon)  # 월
print('tm_mday : ', gt.tm_mday)  # 일
print('tm_hour : ', gt.tm_hour)  # 시
print('tm_min : ', gt.tm_min)  # 분
print('tm_sec : ', gt.tm_sec)  # 초
print('tm_wday : ', gt.tm_wday)  # 요일
