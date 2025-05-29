from http.server import BaseHTTPRequestHandler, HTTPServer

class PingHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/ping":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Pong")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

if __name__ == "__main__":
    server_address = ("0.0.0.0", 8085)
    httpd = HTTPServer(server_address, PingHandler)
    print("Server running on port 8085...")
    httpd.serve_forever()

