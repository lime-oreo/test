peopleNumber = int(input('인원수를 입력하세요. '))

if peopleNumber == 1:
    print('400,000원 지원')
elif peopleNumber == 2:
    print('600,000원 지원')
elif peopleNumber == 3:
    print('800,000원 지원')
elif peopleNumber >= 4:
    print('1,000,000원 지원')
