class Calculator:				       # 클래스 선언

    def __init__(self, n1, n2):		                    # 속성 정의
        print('\n=== __init__() START ===')
        self.num1 = n1
        self.num2 = n2

    def add(self):				       # 메서드 정의
        print('\n=== add() START ===')
        print('num1 + num2 =', self.num1 + self.num2)

    def subtract(self):			       # 메서드 정의
        print('\n=== subtract() START ===')
        print('num1 - num2 =', self.num1 - self.num2)

calc1 = Calculator(10, 20)		# 객체 생성
calc2 = Calculator(100, 200)  	# 객체 생성
calc3 = Calculator(1000, 2000)	# 객체 생성

print('calc1.num1 :', calc1.num1)   # calc1의 num1에 접근
print('calc1.num2 :', calc1.num2)   # calc1의 num2에 접근

print('calc2.num1 :', calc2.num1)   # calc2의 num1에 접근
print('calc2.num2 :', calc2.num2)   # calc2의 num2에 접근

print('calc3.num1 :', calc3.num1)   # calc3의 num1에 접근
print('calc3.num2 :', calc3.num2)   # calc3의 num2에 접근
