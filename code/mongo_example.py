from mongo import MongoDBInstance
from datetime import datetime

DB = 'searchlight'
COLLECTION = 'articles'
mongo = MongoDBInstance(db=DB, coll=COLLECTION)

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
	mongo.create(example)
except Exception as e:
	print e

try:
	record = mongo.read(obj_id=1)
	print type(record)

except Exception as e:
	print e

try:
	mongo.update(example)
except Exception as e:
	print e

# try:
# 	mongo.delete(example)
# except Exception as e:
# 	print e





