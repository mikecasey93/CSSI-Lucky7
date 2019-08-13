from google.appengine.ext import ndb


class Lottery(ndb.Model):
	n1 = ndb.IntegerProperty(required=True)
	n2 = ndb.IntegerProperty(required=True)
	n3 = ndb.IntegerProperty(required=True)
	n4 = ndb.IntegerProperty(required=True)
	n5 = ndb.IntegerProperty(required=True)
	n6 = ndb.IntegerProperty(required=True)
	date = ndb.StringProperty(required=True)
