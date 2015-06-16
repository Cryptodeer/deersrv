Deersrv
=======

Python plugin for deerwallet


Install
-------

clone & python setup.py install

Usage
-----

```
from flask import Flask, request, jsonify
import deersrv
import json

application = Flask(__name__)

@application.route("/deerwallet", methods=["POST"])
def deerwalletpost():
    return jsonify(deersrv.proc(request.data))

if __name__ == "__main__":
    application.run(host='127.0.0.1')
```