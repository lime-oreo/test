def fun1():
    print('fun1 함수를 호출합니다!')

def fun2():
    print('fun2 함수를 호출합니다!')

def fun3():
    fun1()
    fun2()
    print('fun3 함수를 호출합니다!')

fun3()
