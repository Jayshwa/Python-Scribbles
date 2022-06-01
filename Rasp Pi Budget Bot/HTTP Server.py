from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO


class YoungHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello, world!")
        print("Responding to http GET request\n")

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        print("Responding to http POST request")
        response = BytesIO()
        response.write(b"This is POST request. ")
        response.write(b"Received: ")
        response.write(body)
        self.wfile.write(response.getvalue())


httpd = HTTPServer(("localhost", 8000), YoungHTTPRequestHandler)
print(f"Serving on 8000")
httpd.serve_forever()

