from tornado.ioloop import IOLoop
from tornado.options import options
from tornado.web import Application
from tornado.log import enable_pretty_logging

from company import CompanyHandler
from food import FoodHandler
from mutual_friends import MutualFriendsHandler


enable_pretty_logging()


def make_app():
    urls = [
        ("/v1/company/employees", CompanyHandler),
        ("/v1/people/mutual_friends", MutualFriendsHandler),
        ("/v1/people/food", FoodHandler)
    ]
    return Application(urls, debug=options.debug)


if __name__ == '__main__':
    app = make_app()
    app.listen(options.port)
    IOLoop.instance().start()
