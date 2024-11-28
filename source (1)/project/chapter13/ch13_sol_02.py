memo = input('메모를 입력하세요. ')

file = open('C:/python/myMemo.txt', 'a')
file.write(memo)
file.close()
