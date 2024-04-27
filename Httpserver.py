from http.server import BaseHTTPRequestHandler, HTTPServer
import json
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"<html><body><h1>Hello, World!</h1></body></html>")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response_data = {'message': 'Data received successfully', 'data': data}
        self.wfile.write(json.dumps(response_data).encode('utf-8'))

def start_server():
    server_address = ('', 8000)
    httpp= HTTPServer(server_address, RequestHandler)
    httpp.serve_forever()

start_server()