"""from flask import Flask, jsonify

app = Flask(__name__)

# 샘플 데이터 (게시물)
posts = [
    {"id": 1, "title": "First Post", "body": "This is the first post."},
    {"id": 2, "title": "Second Post", "body": "This is the second post."}
]

# 모든 게시물 가져오기 (GET 요청)
@app.route('/posts', methods=['GET'])
def get_posts():
    return jsonify(posts)

if __name__ == '__main__':
     app.run(host='0.0.0.0',debug=True)"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'sungusn\'s home'

@app.route('/hello')
def hello():
    return 'Hello,Flask!'
