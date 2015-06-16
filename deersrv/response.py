
class Response():
	"""docstring for ClassName"""
	def __init__(self, r, e=None):
		self.r = {'response':r, 'error':e}

	def setKey(self, k, v):
		self.r[k] = v
		return self

	def get(self):
		return self.r