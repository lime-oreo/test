num = 1
minNum = 0;

while num <= 100:
    if num % 3 == 0 and num % 8 == 0:
        print('공배수 : ', num)
        if minNum == 0: minNum = num
    num += 1

print('최소공배수 : ', minNum)
