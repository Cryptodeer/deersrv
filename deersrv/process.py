import json
from pybitcointools import *
from hashlib import sha256
from .error import Error
from .response import Response
def proc(j):
	try:
		j = re.sub(r"'", r'"', j)
		#return j
		data = json.loads(j)
		if 'params' not in data:
			raise Error('INVALID_REQUEST_PARAMS')
		params = data["params"]
		if checkSig(params):
			try:
				import sys
				current_module = sys.modules[ "deersrv" ]
				#raise exception for attr inx
				toCall = getattr(current_module, params[0])
				s, r, e = toCall(params)
				if s:
					raise Response(r, e)
				else:
					raise Error(e)
			except:
				raise Error('INVALID_REQUEST_TYPE')
	except Error as er:
		return er.get()
	except Response as res:
		return res.get()
		

def checkSig(params):
	try:
		if hasattr(params, "__len__") == False:
			return False
		if isinstance(params, basestring):
			return False
		if len(params) < 4:
			return False
		if params[0] != "CreateTransaction": 
			tohash = params[1]+str(params[2])+params[3]
			dsig = params[4]
		else:
			tohash = params[1]+params[2]+params[3]+str(params[4])+str(params[5])+params[6]
			dsig = params[7]
		pbkstr = str(params[1])
		pbk = decode_pubkey(pbkstr, ( "hex" if len(pbkstr) > 74 else "hex_compressed" ) )
		mhash = sha256(sha256(tohash).digest()).digest()
		try:  
			o, r, s = decode_sig(dsig)
		except: 
			import ecdsa
		 	r, s = ecdsa.util.sigdecode_der(dsig.decode("hex"), 0)
		 	o = 0
		else:
			raise
		if ecdsa_raw_verify(mhash, (o, r, s), pbk):
			return True
		else:
			raise
	except:
		raise Error('INVALID_SIGNATURE')
