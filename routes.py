from tornado.web import url
from controllers import *

routes = [


    # WEB
    url('/', MainPageHandler, name='index'),

    # API


]
