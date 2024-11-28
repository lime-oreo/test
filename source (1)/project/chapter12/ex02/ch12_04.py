import convertUnitModule as cu    # convertUnitModule을 cu로 치환한다.

inputData = int(input('길이(mm)를 입력하세요. '))

result = cu.convertUnit(inputData)
cu.printLength(inputData, result)
