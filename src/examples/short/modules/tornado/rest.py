"""
rest.py
"""

import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):  # pyrefly: ignore[bad-override]
        self.write("Hello, World!")

    def data_received(self, _data):  # pyrefly: ignore[bad-param-name-override]
        pass


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
