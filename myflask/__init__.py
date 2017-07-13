from flask import Flask

print('name :', __name__)
app = Flask(__name__)


# register view function of get method request
@app.route('/')
def hello_world():
    return 'Hello World'

