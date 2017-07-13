from wsgiref.simple_server import make_server


def app(env, res):
    res_body = ['%s: %s' % (k, v) for k, v in sorted(env.items())]
    res_body = '\n'.join(res_body)
    # res_body = 'hello world'

    status = '200 OK'
    res_headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(res_body)))]
    res(status, res_headers)

    return [res_body.encode('utf8')]

httpd = make_server('localhost', 8080, app)

# server shutdown as soon as it gets the first request
httpd.handle_request()

