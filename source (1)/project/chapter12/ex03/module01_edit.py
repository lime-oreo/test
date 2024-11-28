def fun():
    print('module01의 함수가 실행됩니다.')

if __name__ == '__main__':                   # 메인 파일이면 실행 한다.
    fun()
    print('__name__ : ', __name__)
