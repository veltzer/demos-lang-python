"""
demo of simple web server in python using HTTPServer
originally grabbed from 'http://fragments.turtlemeat.com/pythonwebserver.php'.
Copyright Jon Berg , turtlemeat.com
"""

import cgi
import os
import threading
import time

import BaseHTTPServer
import SocketServer


class ThreadedServer(SocketServer.ThreadingMixIn, BaseHTTPServer.HTTPServer):
    """Handle requests in a separate thread."""
    pass


class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
    def __init__(self):
        super(MyHandler).__init__()
        self.real_path = None

    def handle_static(self, mimetype):
        f = open(self.real_path)
        # note that this potentially makes every file on your computer
        # readable by the internet. A real web server also checks that
        # the file that it is serving is inside into service 'realm'.
        self.send_response(200)
        self.send_header('Content-type', mimetype)
        self.end_headers()
        self.wfile.write(f.read())
        f.close()

    def handle_esp(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('time is the ' + str(time) + '<br/>')
        self.wfile.write('today is the ' + str(time.localtime()[7]) + '<br/>')
        self.wfile.write(
            'day in the year ' + str(time.localtime()[0]) + '<br/>')

    def handle_dir(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write('<html><body>')
        for x in os.listdir(self.real_path):
            ref = 'http://localhost:8001' + self.path + x
            self.wfile.write('<a href=\'' + ref + '\'>' + x + '</a><br/>')
        self.wfile.write('</body></html>')

    def get(self):
        # our dynamic content
        if self.path.endswith('.esp'):
            self.handle_esp()
            return
        # add a '.' to path to make it a local file path
        # /->./
        # /index.html -> ./index.html
        self.real_path = '.' + self.path
        if os.path.isfile(self.real_path):
            # our static HTML content
            if self.path.endswith('.html'):
                self.handle_static('text/html')
                return
            # our static icons content
            if self.path.endswith('.ico'):
                self.handle_static('image/vnd.microsoft.icon')
                return
            # unrecognized file suffix
            self.send_error(
                500, 'Unrecognized file type: {0}'.format(self.path))
            return
        if os.path.isdir(self.real_path):
            self.handle_dir()

    def do_GET(self):
        print(threading.current_thread())
        # this is the method called by the framework... any lower level error
        # should send internal error to the client...
        try:
            self.get()
        except Exception as e:
            self.send_error(
                500, 'GET Internal server error for resource: {0} {1}'.format(self.path, e))

    def do_POST(self):
        try:
            ctype, pdict = cgi.parse_header(
                self.headers.getheader('content-type'))
            if ctype == 'multipart/form-data':
                query = cgi.parse_multipart(self.rfile, pdict)
            else:
                raise ValueError("not a form")
            self.send_response(301)
            self.end_headers()
            upfilecontent = query.get('upfile')
            # print('filecontent', upfilecontent[0])
            self.wfile.write('<html><body>POST OK.<br/><br/>')
            self.wfile.write('<b>file content is:</b><br/><code>')
            self.wfile.write(upfilecontent[0])
            self.wfile.write('</code></body></html>')
        except Exception as e:
            self.send_error(
                500, 'POST Internal server error for resource: {0} {1}'.format(self.path, e))


def main():
    host = 'localhost'
    port = 8001
    url = 'http://' + host + ':' + str(port)
    print('constructing server')
    threaded = True
    # threaded=False
    if threaded:
        server = ThreadedServer((host, port), MyHandler)
    else:
        server = BaseHTTPServer.HTTPServer((host, port), MyHandler)
    try:
        print('contact me at ' + url)
        server.serve_forever()
    except KeyboardInterrupt:
        print()
        print()
        print('CTRL+C received, shutting down server')
        server.socket.close()


main()
