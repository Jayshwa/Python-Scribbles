from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os

PORT = []
file_dir = os.path.join(os.path.dirname(__file__))
file_name = os.path.basename(__file__)
abs_path = os.path.join(file_dir, file_name)

# breakpoint()

with open(os.path.join(file_dir, "login.json"), "r", encoding="utf-8") as login:
    TOKEN = json.load(login)
    PORT.append(TOKEN["port"])


class Serv(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write("Hello Josh".encode())


def main():
    server = HTTPServer(("", int(PORT[0])), Serv)
    print(f"Server running on port {int(PORT[0])}")
    server.serve_forever()


if __name__ == "__main__":
    main()
