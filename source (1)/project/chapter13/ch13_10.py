file = open('C:/python/number.txt', 'r')
result = file.read()
print('result :', result)
sum = int(result) + 1
print('sum :', sum)
file.close()
