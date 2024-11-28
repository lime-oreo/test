file = open('C:/python/test.txt', 'w')		# 파일 열기(쓰기 모드)
result = file.write('Hello python~')		# 쓰기
print('type of result :', type(result))		# 반환값 데이터 타입
print('result :', result)			# 반환값 출력
file.close()				# 파일 닫기
