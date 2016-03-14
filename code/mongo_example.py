from mongo import MongoDBInstance
from datetime import datetime
from pprint import pprint

DB = 'searchlight'
COLLECTION = 'articles'
HOST = 'localhost'
PORT = 27017
mongo = MongoDBInstance(db=DB, coll=COLLECTION, h=HOST, p=PORT)

example = {
	"title": "Example Schema",
	"type": "object",
	"timestamp": datetime.now(),
	"properties": {
		"firstName": {
			"type": "string"
		},
		"lastName": {
			"type": "string"
		},
		"age": {
			"description": "Age in years",
			"type": "integer",
			"minimum": 0
		}
	},
	"required": ["firstName", "lastName"]
}

try:
	record = mongo.create(example)
except Exception as e:
	print e

try:
	result = mongo.read(obj_id=record)
	for record in result:
		pprint(record)
except Exception as e:
	print e

try:
	mongo.update(example)
except Exception as e:
	print e

try:
	mongo.delete(example)
except Exception as e:
	print e





