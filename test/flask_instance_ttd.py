"""
A list of things to do from flask instance

    - 1. global instance
    - 2. creation of user response instance for common http response
    - 3. Management decorator of before and after http request
    - 4. custom url converter, BaseConverter
    - 5. WSGI middleware
    - 6. debug mode
    - 7. view function
    - 8. logger
    - 9. test server
    - 10. template filter
    - 11. HTTP error handler
    - 12. Blueprint
    - 13. test client
"""

"""
1. global instance
g is an instance of app_ctx_globals_class.
"""
from flask import g
from myflask import app


def connect_db():
    # return sqlite3.connect(app.config['DATABASE'])
    pass


# possible to declare multiple functions with these decorators.
@app.before_request
def before_request():
    g.db = connect_db()


@app.teardown_request
def teardown_request(e):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

"""
2. creation of user response instance for common http response
use make_response supporting response_class, str, unicode(only for python2), WSGI function, tuple
"""

from flask import Response, make_response


# 2-1. response class
@app.route('/')
def response_class():
    custom_response = Response('custom res', 200, {'header1': 'header test 1'})
    return make_response(custom_response)


# 2-2. str
@app.route('/')
def response_str():
    return make_response('str response')


# 2-3. WSGI function providing more specific low controls
@app.route('/')
def response_wsgi():

    def wsgi_app(env, res):
        res_body = 'The request method was %s' % env['REQUEST_METHOD']
        status = '200 OK'
        res_headers = [('Content-Type', 'text/plain'), ('Content-length', str(len(res_body)))]
        res(status, res_headers)
        return [res_body]

    return make_response(wsgi_app)


# 2-4. tuple(response instance, status code/text, response header), easy to modify state and header
@app.route('/')
def response_tuple():
    return make_response(('Tuple custom response', 'OK', {'res_method': 'Tuple res'}))

"""
3. Management decorator of before and after http request
    - before_first_request
    - before_request
    - after_request
    - teardown_request: after response to browser
    - teardown_appcontext: after complete http response, the executed in application contexnt
"""


@app.route('/')
def http_prepost_res():
    return '/'


@app.before_first_request
def before_first_request():
    print('first http request')


@app.before_request
def before_request():
    print('before every http request handled')


@app.after_request
def after_request(res):
    print('after every http request handled')


@app.teardown_request
def teardown_request(e):
    print('after every browser response')


@app.teardown_appcontext
def teardown_appcontext(e):
    print('Called when request application context is ended. In other words, it is executed after teardown_request '
          'usually used eliminating instances.. quite limited usages. '
          'The functions using this decorator are added to teardown_appcontext_funcs as element of list')


"""
5. WSGI converter
    - http Environ resetting and new request path
    - execute exterior apps
    - load balancing and remote processing
    - contents pre processing
"""

import logging


class LogMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, env, res):
        url = env.get('PATH_INFO', '')

        query = env.get('QUERY_STRING', '')

        item = logging.LogRecord(
            name='logname',
            level=logging.INFO,
            pathname=url,
            lineno='',
            msg=query,
            args=None,
            exc_info=None
        )

        return self.app(env, res)

# reassign middleware
app.wsgi_app = LogMiddleware(app.wsgi_app)

"""
6. debug mode

"""

app.debug = True

app.config.update(DEBUG=True)







