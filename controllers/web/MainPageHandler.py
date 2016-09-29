from controllers import BaseHandler
from controllers.api import ChatSocketHandler

class MainPageHandler(BaseHandler):
    def get(self):
        self.render("index.html", messages=ChatSocketHandler.cache)
