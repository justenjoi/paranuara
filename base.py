import json

from _options import define_options

from pymongo import MongoClient

from tornado.options import options
from tornado.web import RequestHandler

define_options()

client = MongoClient(options.mongo_server, options.mongo_port)

db = client[options.database]


class BaseHandler(RequestHandler):
    """Base handler for all requests. Each endpoint's class should inherit from this"""

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)

        self.companies_collection = db['companies']
        self.people_collection = db['people']

    def data_received(self, chunk):
        pass

    def respond(self, error=None, message=None, finish=True, **kwargs):
        """Base format for responses"""
        response_template = {
            'meta': {
                'error': error,
                'message': message
            }
        }

        if kwargs:
            response_template.update(kwargs)

        self.write(json.dumps(response_template))

        if finish:
            self.finish()

    @staticmethod
    def filter_people_for_request(people, view=None):
        """Given a view, strip out un-wanted keys from the people docs"""
        mandatory_fields = ['_id']

        people_views = {
            'basic': ['name', 'age', 'address', 'phone']
        }

        view = mandatory_fields + people_views.get(view, [])

        for person in people:
            for key in list(person.keys()):
                if key not in view:
                    person.pop(key)

        return people
