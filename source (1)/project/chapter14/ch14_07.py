playerAgeList = [18, 20, 17, 18, 22, 27, 23, 25, 27, 27, 27]

for currentIndex in range(0, len(playerAgeList)):
    max = playerAgeList[currentIndex]
    maxIndex = currentIndex

    for compareIndex in range(currentIndex, len(playerAgeList)):
        if playerAgeList[compareIndex] >= max:
            max = playerAgeList[compareIndex]
            maxIndex = compareIndex

    max = playerAgeList[maxIndex]
    playerAgeList[maxIndex] = playerAgeList[currentIndex]
    playerAgeList[currentIndex] = max

print(playerAgeList)
print('가장 많은 나이 : ', playerAgeList[0])
print('가장 적은 나이 : ', playerAgeList[len(playerAgeList) - 1])
