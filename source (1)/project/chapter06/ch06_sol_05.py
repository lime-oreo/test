print('1.월~금, 2.토요일, 3.공휴일')
dayWeek = int(input('요일을 선택하세요. '))

if dayWeek == 1:
    print('버스전용차로 단속 중입니다.')
    print('1.버스, 2.승용차')
    carType = int(input('차종을 선택하세요. '))

    if carType != 1:
        print('버스전용차로 위반!!')
    else:
        print('버스입니다.')
else:
    print('토요일 및 공휴일은 단속하지 않습니다.')
