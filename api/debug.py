from http.server import BaseHTTPRequestHandler
import json
import os

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Configurar respuesta
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
        # Estado del servidor
        status = {
            "status": "ok",
            "environment": {
                "VERCEL": os.environ.get('VERCEL', 'Not set'),
                "DJANGO_SETTINGS_MODULE": os.environ.get('DJANGO_SETTINGS_MODULE', 'Not set'),
                "DEBUG": os.environ.get('DEBUG', 'Not set')
            },
            "message": "API de Lista de Tareas funcionando correctamente"
        }
        
        # Enviar respuesta
        self.wfile.write(json.dumps(status).encode())
        return 