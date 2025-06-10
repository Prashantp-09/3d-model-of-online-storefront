import http.server
import socketserver

PORT = 8000
handler = http.server.SimpleHTTPRequestHandler

print(f"Server running at http://localhost:{PORT}")
with socketserver.TCPServer(("", PORT), handler) as httpd:
    httpd.serve_forever()
