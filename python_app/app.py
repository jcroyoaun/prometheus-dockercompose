import http.server
from prometheus_client import start_http_server, Counter

REQUEST_COUNT = Counter('app_request_count', 'Total app http request count')
APP_PORT = 8000
METRICS_PORT = 8001

class HandleRequests(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        REQUEST_COUNT.inc()
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Mi aplicacion instrumentada</title></head><body><center><h2>Cerouno - Demo de instrumentation para Prometheus con Python.</center></h2></body></html>", "utf-8"))
        self.wfile.close()

if __name__ == "__main__":
    start_http_server(METRICS_PORT)
    server = http.server.HTTPServer(('0.0.0.0', APP_PORT), HandleRequests)
    server.serve_forever()
