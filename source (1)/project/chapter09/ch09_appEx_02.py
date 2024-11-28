members = {}
flag = True

while flag:
    selectNum = int(input('\n1. 회원가입, 2. 프로그램 종료\t'))
    
    if selectNum == 1:
        id = input('아이디를 입력하세요.\t')
        pw = input('비밀번호를 입력하세요.\t')
        members[id] = pw
        
    elif selectNum == 2:
        print('-' * 30)
        print('아이디 : 비밀번호')
        print('-' * 30)
        
        for key in members.keys():
            print(key, '\t:\t', members[key])
        print('-' * 30)
        
        flag = False
