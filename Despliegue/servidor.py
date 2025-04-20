import http.server
import socketserver

PORT = 8080
DIRECTORIO = "../App"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORIO, **kwargs)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor disponible en http://localhost:{PORT}/lista_final.m3u")
    httpd.serve_forever()

