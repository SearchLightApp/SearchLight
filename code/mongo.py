import pymongo 

 
class MongoDBInstance(object):

	def __init__(self, **kwargs):
		self.client = self.client()
		self.database = self.client[kwargs['db']]
		self.collection = self.database[kwargs['coll']]

	def client(self):
		try:
			print 'Connected to mongo instance.'
			return self._get_conn()

		except pymongo.errors.ConnectionFailure, e:
			print "Could not connect to server: %s" % e
			sys.exit()

	def _get_conn(self):	
		try:
			mongodb = pymongo.MongoClient(host='localhost', port=27017)

			print 'Connected to db and collection.'
			return mongodb
		except pymongo.errors.ConnectionFailure:
			print "Could not connect to either database or collection: %s" % e 
			sys.exit()

	def create(self, obj):
		if obj is not None:
			print 'Created record'
			self.collection.insert(obj)
		else:
			raise Exception("Did not create record.")
 
 
	def read(self, obj_id=None):
		if obj_id is None:
			print 'Found record(s).'
			return self.collection.find({})
		else:
			return self.collection.find({"_id":obj_id})
 
 
	def update(self, obj):
		if obj is not None:
			print 'Updated record(s).'
			self.collection.save(obj)			
		else:
			raise Exception("Did not update record.")
 
 
	def delete(self, obj):
		if obj is not None:
			print 'Deleted'
			self.collection.remove(obj)			
		else:
			raise Exception("Did not delete record.")