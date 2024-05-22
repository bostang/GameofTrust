from http.server import SimpleHTTPRequestHandler, HTTPServer
import urllib.parse
import threading
import socket
import logging
server_ip = "10.8.102.108"

logging.basicConfig(
    filename='server.log',        # Log file name
    level=logging.DEBUG,          # Log level
    format='%(asctime)s %(levelname)s %(message)s'  # Log format
)


# HTTP Server setup
class MyHTTPRequestHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        logging.info('Received GET request')
        parsed_path = urllib.parse.urlparse(self.path)
        query = urllib.parse.parse_qs(parsed_path.query)
        user_data = query.get('data', [''])[0]
        logging.info(f'Received data: {user_data}')
        # print('Received GET request')
        # print('Path:', self.path)
        # print('Headers:\n', self.headers)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello from HTTP server!')


def run_http_server():
    server_address = (server_ip, 8080)
    httpd = HTTPServer(server_address, MyHTTPRequestHandler)
    print('HTTP server running on port 8080')
    httpd.serve_forever()

# Socket Server setup
def run_socket_server():
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, 65432))
    server_socket.listen(2)  # Listen for up to 2 connections
    print('Socket server running on port 65432')
    
    while True:
        client_socket, addr = server_socket.accept()
        print(f'Connected by {addr}')
        logging.info(f'Connected by {addr}')
        data = client_socket.recv(1024)
        
        if data:
            print('Received data:', data.decode())
            logging.info(f'Received data: {data.decode()}')
        client_socket.sendall(b'Hello from Socket server!')
        client_socket.close()

# Run both servers concurrently
http_thread = threading.Thread(target=run_http_server)
socket_thread = threading.Thread(target=run_socket_server)

http_thread.start()
socket_thread.start()

http_thread.join()
socket_thread.join()
