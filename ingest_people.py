import json

from _options import define_options

from tornado.options import options
from pymongo import MongoClient, ASCENDING


define_options()

client = MongoClient(options.mongo_server, options.mongo_port)

db = client[options.database]
people_collection = db['people']

fruit = ["apple", "banana", "strawberry", "orange"]
vegetables = ["cucumber", "beetroot", "carrot", "celery", "lettuce"]

try:
    with open('./people.json') as people_file:
        people_data = json.load(people_file)

        for p in people_data:
            favourite_veg = []
            favourite_fruit = []

            for food in p.get('favouriteFood', []):
                if food in fruit:
                    favourite_fruit.append(food)
                elif food in vegetables:
                    favourite_veg.append(food)

            p.pop('favouriteFood')
            p['favourite_fruit'] = favourite_fruit
            p['favourite_veg'] = favourite_veg

        people_collection.insert_many(people_data)

    # While an array lookup would be nice and snappy... modifying docs in mongo could change the order and make this
    # unreliable. So lets create an index on the index field instead
    people_collection.create_index([('index', ASCENDING)], unique=True)
except Exception as e:
    print("Something went wrong with the ingest: {}".format(e))
else:
    print("Done!")
