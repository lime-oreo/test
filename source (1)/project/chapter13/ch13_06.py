class Member:
    def __init__(self, i, p):
        self.mId = i
        self.mPw = p
        
class MemberManage:
    def __init__(self):
        self.members = {}

    def addMember(self, m):
        self.members[m.mId] = m.mPw

    def loginMember(self, i, p):
        isMember = i in self.members

        print('====== 로그인 결과 ======')
        if isMember and self.members[i] == p:
            print(i,'님 로그인 성공')
        else:
            print(i, '님 ID와 PW를 다시 확인하세요!')
    
    def removeMember(self, i, p):
        del self.members[i]

    def printMembers(self):
        print('====== 전체 회원 ======')
        for member in self.members.keys():
            print('ID :', member)
            print('PW :', self.members[member])
            print('-----------------------')

mm = MemberManage()


mm.addMember(Member('chanho@gmail.com', '1234a!'))	
mm.addMember(Member('seri@gmail.com', '5678b^'))	
mm.addMember(Member('heungmin@gmail.com', '9852c#'))	

mm.printMembers()	# 전체 회원 출력


mm.loginMember('chanho@gmail.com', '1234a!')		
mm.loginMember('seri@gmail.com', '99999')		


mm.removeMember('chanho@gmail.com', '1234a!')		
mm.removeMember('heungmin@gmail.com', '9852c#')		

mm.printMembers()	# 전체 회원 출력
