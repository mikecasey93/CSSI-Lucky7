from google.appengine.ext import ndb


class Lottery(ndb.Model):
	n1 = ndb.IntegerProperty(required=True)
	n2 = ndb.IntegerProperty(required=True)
	n3 = ndb.IntegerProperty(required=True)
	n4 = ndb.IntegerProperty(required=True)
	n5 = ndb.IntegerProperty(required=True)
	n6 = ndb.IntegerProperty(required=True)
	date = ndb.StringProperty(required=True)

	def __eq__(self, other):
		if self.n1 == other.n1 and self.n2 == other.n2 and self.n3 == other.n3 and self.n4 == other.n4 and self.n5 == other.n5 and self.n6 == other.n6 and self.date == other.date:
			return True
		else:
			return False