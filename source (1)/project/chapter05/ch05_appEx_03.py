# 3 * 8 = computer * time
# computer = 3 * 8 / time

time = int(input('단축 근무시간을 입력하세요.'))

computer = 3 * 8 // time
addComputer = 1 if (3 * 8 % time) > 0 else 0

print('필요한 컴퓨터 : ', computer + addComputer)
