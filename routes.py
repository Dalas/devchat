from tornado.web import url
from controllers import *
from tornado.web import StaticFileHandler


routes = [

    # Static files.
    url(r'/static/', StaticFileHandler, {'path': './static'}),

    # WEB
    url('/', MainPageHandler, name='index'),

    # API

    # CHAT

    (r"/chatsocket", ChatSocketHandler),

]
