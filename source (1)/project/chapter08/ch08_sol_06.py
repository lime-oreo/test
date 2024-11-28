fruits = ['사과', '망고', '당근', '수박', '포도', '참외', '토마토']
print("fruits : ", fruits)

for item in fruits:
    if item == '당근' or item == '토마토':
        fruits.remove(item)

print("fruits : ", fruits)
