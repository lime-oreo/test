"""""import requests

x = requests.get('https://w3schools.com/python/demopage.htmㅣ')

print(x.text)"""

"""import requests
user_id = 1
# URL 설정
url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"  # 1번 게시물을 조회

# GET 요청 보내기 #이게 웹 클라이언트 자체임.
response = requests.get(url) 

# 응답 상태 코드 확인
if response.status_code == 200: #상태값
    # JSON 데이터 파싱
    data = response.json()
    for i in data : 
        if i == 'id':
            print("Post ID:", data[i])
        elif i == 'title':
            print("Title:", data[i])
        elif i == 'body':
            print("Body:", data[i])
    # 결과 출력
    print("Post ID:", data['id'])
    print("Title:", data['title'])
    print("Body:", data['body'])
else:
    print("Failed to retrieve data. Status code:", response.status_code)



print(type(data))"""

import requests

user_id = 1
# URL 설정
url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"

# GET 요청 보내기
response = requests.get(url)

# 응답 상태 코드 확인
if response.status_code == 200:
    # JSON 데이터 파싱
    data = response.json()
    
    # 가져온 게시물 개수 출력
    print(f"Total posts retrieved: {len(data)}\n")
    
    # 각 게시물의 ID와 제목 출력 (최대 5개까지만 출력)
    for post in data[:5]:  # 처음 5개 게시물만 출력
        print(f"Post ID: {post['id']}, Title: {post['title']}")
else:
    print("Failed to retrieve data. Status code:", response.status_code)