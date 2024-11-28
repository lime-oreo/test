import operator
import calculator as ca      # calculator 모듈을 가져온다.

num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

op = input("연산자를 입력하세요 (+, -, *, /): ")
#print(type(op))

# def add(a,b):

#     def divOperator(num1,num2):
#         pass

#     if type(a) != float:
#         print('실수가 아닙니다.')
#         return -1
#     if type(b) != float:
#         print('실수가 아닙니다.')
#         return -1
#     return a+b

# print(sep='')

#result = 0 선언을 따로 하지 않아도 아래 if else에서 쓸수 있음(파이썬이 해주는 것)

if op == '+' :
    result = ca.addition(num1, num2)

    #num1 + num2
    #result = operator.add(num1, num2)

    # ret = add('num1',num2)
    # if(ret != -1):
    #     print(ret)
elif op == '-' :
    result = ca.subtraction(num1, num2)
    #print(num1 - num2)
elif op == '*' :
    result = ca.multiplication(num1, num2)
    #print(num1 * num2)
elif op == '/' :
    result = ca.division(num1, num2)
    #print(num1 / num2)
else:
    print('연산자를 확인해주세요.')

print(result)