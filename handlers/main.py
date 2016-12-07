from handlers.base import BaseHandler
import logging

logger = logging.getLogger()


class MainHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        unhashed_password = self.get_argument("inputPassword")
        username = self.get_argument("inputUser")
        email = self.get_argument("inputEmail")
        # todo: log data
        # todo: show d3 bars

        self.render("home.html")

