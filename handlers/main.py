from handlers.base import BaseHandler
import bcrypt
import logging
import threading

logger = logging.getLogger()


class MainHandler(BaseHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        unhashed_password = self.get_argument("inputPassword").encode('utf-8')
        username = self.get_argument("inputUser")
        email = self.get_argument("inputEmail")

        # move blocking hashing of password to own thread
        thread = threading.Thread(target=self.hash_password, args=(username, unhashed_password, email))
        thread.start()

        self.render("home.html")

    def hash_password(self, username, password, email):
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        logger.info("%s; %s; %s", username, hashed_password, email)