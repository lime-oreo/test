file = open('C:/python/test.txt', 'r')		# 파일 열기(읽기 모드)
result = file.read()			             # 읽기
print('type of result :', type(result))		# 반환값 데이터 타입
print('result :', result)			
file.close()				
