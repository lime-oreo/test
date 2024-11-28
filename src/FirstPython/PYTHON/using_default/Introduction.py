#print("이름 : 구성순")
#print("사는곳 : 서울시 중랑구")  
#print("전공 : 응용생명과학")
#print("수강목적 : 유전자검사 관련 일을 하고 있는데, 생물정보학 (Bioinformatics)과 관련된 업무를 하고 싶어서 수강신청 하였습니다!") 
#print("주변맛집 : 이 뒷편에 미나리 떡볶이집 하이볼이랑 먹으니깐 맛있었어요 !")
"""
#input 함수활용법
my_name=(input("본인 이름:" )) #input 변수선언 필요
my_ad=(input("사는 곳:" ))
my_major=(input("전공:"))
my_goal=(input("수강 목적:"))
my_fv=(input("주변맛집:"))
print(f'본인 이름 : {my_name}')
print(f'본인 주소: {my_ad}')
print(f'본인 전공: {my_major}')
print(f'본인 목적: {my_goal}')
print(f'주변 맛집: {my_fv}')

"""


# 추가강의때 엑셀에 추가하기 혹은 DBL에 추가하기 할 예정

while True :
    exit_input=input ('입력을 계속 하시겠습니까? : \n(계속하려면 ENTER ,종료하려면 종료입력.)')
    if exit_input=='종료':
        print('프로그램을 종료합니다.')
        break  #while loop을 빠져나옴
    my_name=(input("본인 이름:" )) #input 변수선언 필요
    my_ad=(input("사는 곳:" ))
    my_major=(input("전공:"))
    my_goal=(input("수강 목적:"))
    my_fv=(input("주변맛집:"))

    print ('====입력정보====\n')
    print(f'본인 이름 : {my_name}')
    print(f'본인 주소: {my_ad}')
    print(f'본인 전공: {my_major}')
    print(f'본인 목적: {my_goal}')
    print(f'주변 맛집: {my_fv}')
    print ('===========\n')
