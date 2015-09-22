# -*- coding: utf-8 -*-

import json
import logging
import sys
import pprint

from flask import current_app, Flask, request, Response

HOST = '127.0.0.1'
PORT = 5000
DEBUG = True


app = Flask(__name__)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.propagate = False
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
format_msg = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(format_msg)
ch.setFormatter(formatter)
logger.addHandler(ch)


@app.route('/callback/<cid>/', methods=['POST'])
def callback(cid):
    data = request.json
    pp = pprint.PrettyPrinter(indent=4)
    current_app.logger.info(pp.pprint("{this}".format(this=data)))
    current_app.logger.info("CID: {cid}".format(cid=cid))
    return Response(json.dumps({'msg': 'ok'}), 200,
                    content_type='application/json')


if __name__ == '__main__':
    msg = "[x] Listening {host}:{port}".format(host=HOST,
                                               port=PORT)
    logger.info(msg)
    app.run(host=HOST, port=PORT, debug=DEBUG)
