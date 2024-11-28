userGrade = int(input('회원 등급을 선택하세요.\n1. VVIP \t2. VIP \t3. GOLD '))
smsCount = int(input('SMS 발송 건수를 입력하세요. '))
mmsCount = int(input('MMS 발송 건수를 입력하세요. '))
smsPrice = 0
mmsPrice = 0

if userGrade == 1:
    smsPrice = 0

    if mmsCount > 50:
        mmsPrice = (mmsCount - 50) * 20
    else:
        mmsPrice = 0
        
elif userGrade == 2:
    if smsCount > 100:
        smsPrice = (smsCount - 100) * 10
    else:
        smsPrice = 0

    if mmsCount > 10:
        mmsPrice = (mmsCount - 10) * 20
    else:
        mmsPrice = 0
        
elif userGrade == 3:
    if smsCount > 10:
        smsPrice = (smsCount - 10) * 10
    else:
        smsPrice = 0

    if mmsCount > 5:
        mmsPrice = (mmsCount - 5) * 20
    else:
        mmsPrice = 0

print('smsPrice :', smsPrice, ' 원')
print('mmsPrice :', mmsPrice, ' 원')
