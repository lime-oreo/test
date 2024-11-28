import mysql.connector
# 데이터베이스에 연결
connection = mysql.connector.connect(
    host="localhost", #본인 PC로 접속
    user="root", #따로 만들지 않았다면 root
    password="0000", #패스워드 ""사이에 넣기 문자열을 이해시키고 pw에 넣어야함.
    database="classicmodels",
    charset='utf8mb4',      # 문자 집합 설정
    collation = 'utf8mb4_general_ci'
)

cursor = connection.cursor()
#이렇게 하면 utf8 문자 에러가 뜸.


cursor.execute("SELECT * FROM customers")
rows = cursor.fetchall()  # 모든 결과 가져오기

for row in rows:
    print(row)
