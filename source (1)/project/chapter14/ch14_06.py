playerAgeList = [18, 20, 17, 18, 22, 27, 23, 25, 27, 27, 27]
playerUnder18 = 0

for playerAge in playerAgeList:
    if playerAge <= 18:
        playerUnder18 += 1

print('18세 이하 선수는', playerUnder18, '명입니다.')
