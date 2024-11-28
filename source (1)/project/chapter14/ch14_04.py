commandStr = input('문자열을 입력하세요.\n')
commandStrList = []
secretList = ['a', 'pp', 'le.']

cnt = 0
strIndex = 0

for c in commandStr:
    commandStrList.append(c)

    strIndex += 1
    if strIndex > 6: strIndex = 1
    
    if strIndex == 1:
        commandStrList.append(secretList[cnt])
        cnt += 1
        
    elif strIndex == 3:
        commandStrList.append(secretList[cnt])
        cnt += 1
        
    elif strIndex == 6:
        commandStrList.append(secretList[2])
        cnt += 1
        if cnt >= 3: cnt = 0

secretCommandStr = ''
for c in commandStrList:
    secretCommandStr += c

print('암호문 : ', secretCommandStr)
