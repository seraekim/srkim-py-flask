from flask import Flask, request, make_response, redirect, abort, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    # return '<h1>Hello World!</h1>'
    return render_template('main.html')


@app.route('/user/<name>')
def user(name):
    if not name:
        abort(404)
    return '<h1>Hello, %s!</h1>' % name


@app.route('/user2/', defaults={'name': 'anonymous'})
@app.route('/user2/<name>')
def user2(name):
    return render_template('user.html', name=name)


@app.route('/bro')
def browser_info():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


@app.route('/400')
def res400():
    return '<h1>Bad Request</h1>', 400


@app.route('/cookie')
def cookie():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response


@app.route('/redir')
def redir():
    return redirect('http://www.naver.com')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('err/404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('err/500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
