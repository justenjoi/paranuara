import json

from pymongo import MongoClient

from _options import define_options
from tornado.options import options


define_options()

client = MongoClient(options.mongo_server, options.mongo_port)

db = client[options.database]
companies_collection = db['companies']

try:
    with open('companies.json') as companies_file:
        company_data = json.load(companies_file)

        companies_collection.insert_many(company_data)
except Exception as e:
    print("Something went wrong with the ingest: {}".format(e))
else:
    print("Done!")
