import http.server
import socketserver

PORT = 8080

httpd = socketserver.TCPServer(('', PORT), http.server.SimpleHTTPRequestHandler)
print('start!!! see at http://localhost:8080')

httpd.serve_forever()
