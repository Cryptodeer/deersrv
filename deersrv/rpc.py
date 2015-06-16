#!/bin/python
import json
import requests
import time
from .costants import *
from .utils import *
from .error import Error
#import logging
def getnewaddress(params, id="local"):
	return rpccall(id, "getnewaddress", params)

def listaccounts(id="local"):
	data = rpccall(id, "listaccounts", [])
	#print data['result']
	return data['result']

def findaccounts(pbk, value=False):
	alist = listaccounts()
	for k, v in alist.items():
		if pbk == k:
			return v if value else True
	return None if value else False

def getbalance(pbk):
	return findaccounts(pbk, value=True)

def sendmany(params, id="local"):
	alias = rpccall(id, "sendmany", params)
	if alias['error'] == None:
		return alias['result']
	else:
		raise

def listtransactions(pbk):
	if findaccounts(pbk):
		return rpccall("local", "listtransactions", [pbk])['result']
	return []

def createaccount(pbk):
	if findaccounts(pbk):
		return None
	gaddr = getnewaddress([pbk])
	#print gaddr['error'], gaddr['result']
	return gaddr['result']

#solo local
def rpccall(id, method, params):
	n_time = numint(time.time())
	s_time = numstr(n_time)
	s_id = id
	postreq = { "id":(s_time+s_id), "params":params, "method": method }
	try:
		data = requests.post((API_PROTOCOL + "://" + API_ENDPOINT + "/" + API_DEERWALLET_PATH), data=json.dumps(postreq), auth=(RPC_USER, RPC_PASSWORD))
		#print data, data.text
		return json.loads(data.text)
	except:
		raise

def testMoney(addr):
	return sendmany(["cashreserve", {addr:[{"Circuit":"EUR", "Amount":10000}]}])