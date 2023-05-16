"""
demo of simple web server in python using HTTPServer
originally grabbed from "http://fragments.turtlemeat.com/pythonwebserver.php".
"""

# pylint: disable=deprecated-module
import cgi
import os
import threading
import time

from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver


class ThreadedServer(socketserver.ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


class MyHandler(BaseHTTPRequestHandler):
    def __init__(self, addr, handler):
        super().__init__(self, addr, handler)
        self.real_path = None

    def handle_static(self, mimetype):
        # note that this potentially makes every file on your computer
        # readable by the internet. A real web server also checks that
        # the file that it is serving is inside into service "realm".
        self.send_response(200)
        self.send_header("Content-type", mimetype)
        self.end_headers()
        with open(self.real_path) as f:
            self.wfile.write(f.read())

    def handle_esp(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("time is the " + str(time) + "<br/>")
        self.wfile.write("today is the " + str(time.localtime()[7]) + "<br/>")
        self.wfile.write(
            "day in the year " + str(time.localtime()[0]) + "<br/>")

    def handle_dir(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><body>")
        for x in os.listdir(self.real_path):
            ref = "http://localhost:8001" + self.path + x
            self.wfile.write("<a href=\"" + ref + "\">" + x + "</a><br/>")
        self.wfile.write("</body></html>")

    def get(self):
        # our dynamic content
        if self.path.endswith(".esp"):
            self.handle_esp()
            return
        # add a "." to path to make it a local file path
        # /->./
        # /index.html -> ./index.html
        self.real_path = "." + self.path
        if os.path.isfile(self.real_path):
            # our static HTML content
            if self.path.endswith(".html"):
                self.handle_static("text/html")
                return
            # our static icons content
            if self.path.endswith(".ico"):
                self.handle_static("image/vnd.microsoft.icon")
                return
            # unrecognized file suffix
            self.send_error(500, f"Unrecognized file type: {self.path}")
            return
        if os.path.isdir(self.real_path):
            self.handle_dir()

    def do_GET(self):
        print(threading.current_thread())
        # this is the method called by the framework... any lower level error
        # should send internal error to the client...
        # pylint: disable=broad-except
        try:
            self.get()
        except Exception as e:
            self.send_error(500, f"GET Internal server error for resource: {self.path} {e}")

    def do_POST(self):
        # pylint: disable=broad-except
        try:
            content_type, options_dict = cgi.parse_header(
                self.headers.getheader("content-type"))
            if content_type == "multipart/form-data":
                query = cgi.parse_multipart(self.rfile, options_dict)
            else:
                raise ValueError("not a form")
            self.send_response(301)
            self.end_headers()
            upload_content = query.get("upload_content")
            # print("upload_content", upload_content[0])
            self.wfile.write("<html><body>POST OK.<br/><br/>")
            self.wfile.write("<b>file content is:</b><br/><code>")
            self.wfile.write(upload_content[0])
            self.wfile.write("</code></body></html>")
        except Exception as e:
            self.send_error(500, f"POST Internal server error for resource: {self.path} {e}")


def main():
    host = "localhost"
    port = 8001
    url = f"http://{host}:{port}"
    print("constructing server")
    threaded = True
    # threaded=False
    if threaded:
        server = ThreadedServer((host, port), MyHandler)
    else:
        server = HTTPServer((host, port), MyHandler)
    try:
        print("contact me at " + url)
        server.serve_forever()
    except KeyboardInterrupt:
        print()
        print()
        print("CTRL+C received, shutting down server")
        server.socket.close()


main()
