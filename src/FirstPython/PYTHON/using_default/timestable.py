"""
print("구구단")
print("2X0=0\n 2x1=1\n 2x2=4\n 2x3=6")
print()
#print("2단 : 2 4 6 8 10 12 14 16 18")
#print("2단: ",2*1, 2*2,2*3,2*4,2*5,2*6,2*7,2*8,2*9)
x = 2
print("2단: ",x*1, x*2,x*3,x*4,x*5,x*6,x*7,x*8,x*9)


#반복문
for i in range(1,10):
    
    print(x*i)

#print("3단 : 3 6 9 12 15 18 21 24 27")
#print("3단 :",3*1,3*2,3*3,3*4,3*5,3*6,3*7,3*8,3*9)
x = 3
print("3단 :",x*1,x*2,x*3,x*4,x*5,x*6,x*7,x*8,x*9)
"""
#while문
'''
x=2
num=1
while num <10 :
    print (x* num)
    num +=1
    
'''

#for문

#x=int(input('출력할 구구단 단 입력 :'))
#for i in range (1,10,1):
  #  print(f'{x}단 : {x}*{i}={x*i}')
  # print(x*i)
  #  print(f'{x}단 : {x}*{i}={x*i}')



"""
printDan 함수로 변경 
for i in range (1,10,1):
    print(f'{x} X {i} = {x*i}')
"""
"""
def printDan(numbers):
    for x in numbers :
    print(f'==={x}단===')

        for i in range (1,10,1):
        print(f'{x} X {i} = {x*i}')

printDan(2)"""

numbers = (2,3,4,5,6,7,8,9)

def printDan(numbers):
    print(f'==={numbers}단===')
    for i in range (1,10,1):
        print(f'{numbers} X {i} = {numbers*i}')


for x in numbers:
    printDan(x)