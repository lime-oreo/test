quiz = (['3+2', 5, 3], ['5나누기2의 몫', 2, 5], ['10-2', 8, 3], ['10의2제곱×2', 200, 5], ['1-(10나누기4의 나머지)', -1, 5], ['2의4제곱', 16, 3], ['4÷2', 2, 3])

answerCount = 0
wrongAnswerCount = 0
totalScore = 0

for item in quiz:
    print('문제 : ', item[0])
    answer = int(input('정답을 입력하세요. '))

    if answer == item[1]:
        answerCount += 1
        totalScore += item[2]
    else:
        wrongAnswerCount += 1

print('-'*30)
print('정답 개수\t: ', answerCount)
print('오답 개수\t: ', wrongAnswerCount)
print('Total Score\t: ', totalScore)
print('-'*30)
