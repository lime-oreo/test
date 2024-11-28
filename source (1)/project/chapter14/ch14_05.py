secretCommandStr = 'aattppackle.sa appt 3le. aampp tole.maorpprowle.'
commandStrList = []
commandStr = ''

for c in secretCommandStr:
    commandStrList.append(c)

commandIndex = 0

for i in range(0, len(commandStrList)):

    if commandIndex == 0:
        commandStr += commandStrList[i]
    elif commandIndex == 2 or commandIndex == 3:
        commandStr += commandStrList[i]
    elif commandIndex == 6 or commandIndex == 7 or commandIndex == 8:
        commandStr += commandStrList[i]

    commandIndex += 1
    if(commandIndex >= 12): commandIndex = 0

print(commandStr)
