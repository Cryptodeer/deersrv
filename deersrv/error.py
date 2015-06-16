import json

class Error():
	errors = {
		'INVALID_PUBLICKEY' : { 'code':101, 'description': "Invalid public key"},
		'INVALID_SIGNATURE' : { 'code':102, 'description': "Invalid signature"},
		'INVALID_REQUEST_PARAMS' : { 'code':103, 'description': "No params included in POST request"},

		'FAILED_CREATE_ACCOUNT' : { 'code':311, 'description': "Failed account creation, please report this error"},
		'INVALID_ADDRESS_ENCODING' : { 'code':312, 'description': "Failed account creation, invalid address encoding"},
		'ACCOUNT_EXISTS' : { 'code':313, 'description': "Failed account creation, accaount already exists"},

		'FAILED_GET_BALANCE' : { 'code':321, 'description': "Failed retriving balance, please report this error"},
		'NEGATIVE_BALANCE' : { 'code':322, 'description': "Failed retriving balance, negative balance"},
		'INVALID_BALANCE_SYNTAX' : { 'code':323, 'description': "Failed retriving balance, invalid balance json syntax"},
		'ACCOUNT_INEXISTENT' : { 'code':324, 'description': "Failed retriving balance, account inexistent"},
		
		'FAILED_LIST_TRANSACTIONS' : { 'code':331, 'description': "Failed listing transactions, please report this error"},
		'INVALID_TXLIST_SYNTAX' : { 'code':332, 'description': "Failed listing transactions, invalid transactions list syntax"},
		
		'FAILED_CREATE_TRANSACTION' : { 'code':341, 'description': "Failed create transaction, please report this error"},
		'FAILED_CREATE_TRANSACTION_FUNDS' : { 'code':342, 'description': "Failed create transaction, insufficient funds"},
		'FAILED_CREATE_TRANSACTION_ADDRESS' : { 'code':343, 'description': "Failed create transaction, invalid address"},
		'FAILED_CREATE_TRANSACTION_CIRCUIT' : { 'code':344, 'description': "Failed create transaction, invalid circuit"},
		'FAILED_CREATE_TRANSACTION_AMOUNT' : { 'code':345, 'description': "Failed create transaction, invalid amount"},
		
		'INVALID_REQUEST_TYPE' : { 'code':401, 'description': "Failed create transaction, invalid amount"},
		'INVALID_ENDPOINT' : { 'code':402, 'description': "the endpoint requested is not avaiable, please visit /help"},

		'UNKNOW_ERROR': { 'code':900, 'description': "An unknow exception has been casted, please report this error"},
	}

	def __init__(self, E="UNKNOW_ERROR", description=None ):
		description = self.errors[E]['description'] if None else description
		for k in self.errors:
			if E == k:
				self.newError = { 'error': E, 'code': self.errors[E]['code'], 'description': description }
				return None
		self.newError = { 'error': E, 'code': 999, 'description': description }
			
	def get(self):
		return self.newError

	def CodeList(self):
		return self.errors

	def Print(self):
		print json.dumps(self.get())

	def triget(self):
		return False, None, self.newError['error']