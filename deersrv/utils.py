# -*- coding: utf-8 -*-
"""
    deerconsole
    ~~~~~

    :copyright: (c) 2015 by Matteo Assinnata
    :license: MIT, see LICENSE for more details.
"""
from hashlib import sha256
import time
import math
import logging

def logme(data, path="/etc/dnet/data/uwsgi/json.log"):
	logging.basicConfig(filename=path,level=logging.DEBUG)
	logging.debug(data)
	return "done"
	
def reverse_hash(hash, hex_format=True):
    """ hash is in hex or binary format
    """
    if not hex_format:
        hash = hexlify(hash) 
    return "".join(reversed(hash))

def numstr(numeric):
	return str(int(math.floor(numeric)))

def numint(numeric):
	return int(math.floor(numeric))
