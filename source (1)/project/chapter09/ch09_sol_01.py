sports = ('태권도', '야구', '농구', '축구', '배구', '권투', '양궁')

for index, item in enumerate(sports):
    if index % 2 == 1:
        print(index, ' : ', item)
