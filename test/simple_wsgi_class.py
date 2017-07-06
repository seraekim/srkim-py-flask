from wsgiref.simple_server import make_server


class App(object):
    def __init__(self, env, res):
        self.env = env
        self.res = res

    def __iter__(self):
        res_body = '\n'.join(['%s: %s' % (k, v) for k, v in sorted(self.env.items())])

        status = '200 OK'
        res_headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(res_body)))]
        self.res(status, res_headers)
        yield res_body.encode('utf-8')

httpd = make_server('localhost', 8080, App)
httpd.serve_forever()

