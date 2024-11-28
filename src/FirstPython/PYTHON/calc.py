#인자 typing
num1= float (input('첫 번째 숫자를 입력하세요 :'))
num2= float (input('두 번째 숫자를 입력하세요 :'))

op= input('연산자를 입력하세요 : (+,-,*,/):')

#함수 호출
def op_sum (num1, num2):
    if type (num1) != float :
        print('not float !')
        return 0
    if type (num2) != float :
        print('not float !')
        return 0
    return num1 + num2

#if문으로 연산자에 따른 argument calculation
if op == '+' :
    #print (num1 + num2)
    op_sum(num1,num2)
elif op == '-':
    print(num1 - num2)

elif op== '*':
    print(num1*num2)

elif op == '/':
    print(num1/num2)

else :
    print('연산자를 확인해주세요.')


# sum 만들기 



x=op_sum(10,20)
print(x)