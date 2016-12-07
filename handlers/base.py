import tornado.web

import logging
logger = logging.getLogger('houser_test.' + __name__)


class BaseHandler(tornado.web.RequestHandler):
    pass
