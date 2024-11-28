scores = {'C/C++':'A', 'Java':'B+', '모바일':'C', '보안':'A+', '해킹':'F', '시스템':'C+'}

print('#시나리오1 ')
print(scores)
print()

print('#시나리오2')
print('Java : ', scores['Java'])
print('시스템 : ', scores['시스템'])
print()

print('#시나리오3 ')
scores['파이썬'] = 'A'
scores['OS'] = 'A+'
print(scores)
print()

print('#시나리오4')
scores['Java'] = 'F'
scores['시스템'] = 'A'
print(scores)
print()

print('#시나리오5')
for key in scores.keys():		       
	print(key, '\t: ', scores[key])
