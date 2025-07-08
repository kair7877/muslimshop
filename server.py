import http.server
import socketserver
import os

os.chdir("/storage/emulated/0/myshop")
PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
    print(f"Открой сайт в браузере: http://localhost:{PORT}")
    httpd.serve_forever()
