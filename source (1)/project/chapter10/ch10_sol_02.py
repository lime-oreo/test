def convertUnit():         # 함수 선언
    print(lengthCm, 'cm = ', lengthCm * 0.393701, 'inch')

lengthCm = float(input('길이를 입력하세요.(cm) '))
convertUnit()             # 함수 호출
