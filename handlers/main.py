from handlers.base import BaseHandler
import logging
import bcrypt

logger = logging.getLogger()


class MainHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        unhashed_password = self.get_argument("inputPassword").encode('utf-8')
        username = self.get_argument("inputUser")
        email = self.get_argument("inputEmail")
        hashed_password = bcrypt.hashpw(unhashed_password, bcrypt.gensalt())
        logger.info("%s; %s; %s", username, hashed_password, email)
        self.render("home.html")
