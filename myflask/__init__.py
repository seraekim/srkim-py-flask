from flask import Flask

print('name :', __name__)
app = Flask(__name__)


# GET 요청에 대해 뷰 함수를 등록
@app.route('/')
def hello_world():
    return 'Hello World'

