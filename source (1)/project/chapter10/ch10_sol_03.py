def calculateDistance():         # 함수 선언
    print('이동 거리는', hourData * speedData, 'km 입니다.')

hourData = float(input('이동 시간을 입력하세요. '))
speedData = float(input('이동 속도를 입력하세요. '))
calculateDistance()             # 함수 호출
