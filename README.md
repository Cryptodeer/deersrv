Deersrv
=======

Python plugin for deerwallet


Install
-------

clone & python setup.py install

Usage
-----

```
from flask import Flask, render_template, request, url_for, jsonify
import deersrv
import json

application = Flask(__name__)

@application.route("/deerwallet", methods=["POST"])
def deerwalletpost():
	#import logging
	#logging.basicConfig(filename='/Users/user/uwsgi.log',level=logging.DEBUG)
	return jsonify(deersrv.proc(json.loads(request.data)))

if __name__ == "__main__":
    application.run(host='127.0.0.1')
```