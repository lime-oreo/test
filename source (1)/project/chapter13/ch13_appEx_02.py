from time import strftime, localtime

def getDay():
    return strftime('%Y-%m-%d', localtime())

def getTime():			
    return strftime('%H:%M:%S', localtime())

print('***************************************')
print('************** 한줄 일기 **************')
print('***************************************')

dFlag =True
while dFlag:
    print('\n다음 항목을 선택하세요.')	
    selectItem = int(input('1.일기작성\t2.일기보기\t3.종료 '))

    if selectItem == 1:
        print('\n[' + getDay() +'] 한줄 일기를 작성하세요.')
        todayDiary = input()

        with open('C:/python/diary.txt', 'a')as f:
            f.write('[' + getDay() + ' ' + getTime() + '] ')
            f.write(todayDiary + '\n')

    elif selectItem == 2:

        with open('C:/python/diary.txt', 'r')as f:
            str = f.read()
            print(str)

    elif selectItem == 3:
        print('\nBye~~')
        dFlag = False
