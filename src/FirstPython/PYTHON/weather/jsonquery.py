import requests

# 1. 모든 게시물 가져오기 (GET 요청)
response = requests.get('http://127.0.0.1:5000/posts')
if response.status_code == 200:
    posts = response.json()
    print("All Posts:", posts)
else:
    print("Failed to retrieve posts.")