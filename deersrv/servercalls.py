from .rpc import createaccount, getbalance, listtransaction, sendmany
from .b58check import is_b58check
from .error import Error
#create account
def CreateAccount(params):
	try:
		ca = createaccount(params[1])
		s, e = ValidateAddress(ca)
		if ca == None:
			raise
		return s, ca, e
	except Error as er:
		return er.triget() 
	except:
		return False, None, 'FAILED_CREATE_ACCOUNT'

def GetBalance(params):
	try:
		balance = getbalance(params[1])
		s, e = False, 'ACCOUNT_INEXISTENT'
		if balance != None:
			s, e = ValidateBalance(balance)
		return s, balance, e
	except:
		return False, None, 'FAILED_GET_BALANCE'

def ListTransactions(params):
	try:
		txlist = listtransaction(params[1])
		s, e = ValidateTxList(txlist)
		return s, txlist, e
	except:
		return False, None, 'FAILED_LIST_TRANSACTIONS'

def CreateTransaction(params):
	try:
		address = params[2]
		circuit = params[3]
		amount = params[4]
		if amount < 0:
			return False, None, 'FAILED_CREATE_TRANSACTION_AMOUNT'
		for v in GetBalance(params):
			if v["Circuit"] == circuit:
				if v["Amount"] >= amount:
					newp = [ params[1], {address:[{circuit:amount}]}, 1]
					rpcre = sendmany(newp)
					s, e = aliastxid(rpcre)
					return s, rpcre, e
				else:
					if v["Amount"] < amount:
						return False, None, 'FAILED_CREATE_TRANSACTION_FUNDS'
		return False, None, 'FAILED_CREATE_TRANSACTION_CIRCUIT'
	except:
		return False, None, 'FAILED_CREATE_TRANSACTION'


def ValidateAddress(addr):
	if is_b58check(addr):
		return True, None
	else:
		return False, 'INVALID_ADDRESS_ENCODING'

def ValidateBalance(balance):
	print balance
	if hasattr(balance, "__len__") == False:
		return False, 'INVALID_BALANCE_SYNTAX'
	if isinstance(balance, basestring):
		return False, 'INVALID_BALANCE_SYNTAX'
	for k,v in balance:
		if k != "Circuit" and k != "Amount":
			return False, 'INVALID_BALANCE_SYNTAX'
		if k == "Amount" and v < 0:
			return False, 'NEGATIVE_BALANCE'
	return True, None

def ValidateTxList(txlist):
	if hasattr(txlist, "__len__") == False:
		return False, 'INVALID_TXLIST_SYNTAX'
	if isinstance(txlist, basestring):
		return False, 'INVALID_TXLIST_SYNTAX'
	return True, None

def aliastxid(rpcre):
	if isinstance(rpcre, basestring):
		return False, 'FAILED_CREATE_TRANSACTION'
	isalias = rpcre.startswith("Transaction succesfully allocated")
	return isalias, None if isalias else 'FAILED_CREATE_TRANSACTION'
