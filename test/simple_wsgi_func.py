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

# 요청을 기다리며 요청 응답 직후 서버 종료
httpd.handle_request()

