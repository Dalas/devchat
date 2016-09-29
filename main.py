from tornado.ioloop import IOLoop
from tornado.web import Application
import logging
from routes import routes
import os

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    filename='devchat.log')

LOGGER = logging.getLogger('app_logger').addHandler(logging.StreamHandler())


def make_app():
    settings = {
        'template_path': os.path.join(os.path.dirname(__file__), "templates"),
        'static_path': os.path.join(os.path.dirname(__file__), "static"),
        'xsrf_cookies': False,
        'debug': True,
        'autoreload': True,
        'compiled_template_cache': False,
        'static_hash_cache': False,
        'cookie_secret': "8fb911c9-0885-4dbf-bedd-921a2b67af08-23a801ee-8556-4f97-8a2b-20916fa92ccd"
    }
    return Application(routes, **settings)


def main():
    app = make_app()
    app.listen(8888)
    io_loop = IOLoop.instance()
    IOLoop.current().start()


if __name__ == "__main__":
    main()
