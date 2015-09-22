# -*- coding: utf-8 -*-

import json
import uuid
import logging
import requests
import sys

from requests.auth import HTTPBasicAuth

fingerprint_path = sys.argv[1]

USER = 'test'
PASSWORD = 'test'
HOST = '127.0.0.1'
PORT = 80
AUTH_URL = "http://{host}:{port}/auth/".format(host=HOST, port=PORT)
IDENTIFY_URL = "http://{host}:{port}/identify/".format(host=HOST, port=PORT)
CALLBACK_ID = str(uuid.uuid1())

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
format_msg = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
formatter = logging.Formatter(format_msg)
ch.setFormatter(formatter)
logger.addHandler(ch)


headers = {'Content-Type': 'application/json;charset=utf-8'}
payload = {'username': USER,
           'password': PASSWORD}
msg = "Posting to auth url ({ur})".format(ur=AUTH_URL)
logger.info(msg)
r = requests.post(AUTH_URL, headers=headers, data=json.dumps(payload))
is_ok = r.status_code == 200

if is_ok:
    data = json.loads(r.content)
    token = data['token']
    fingerprint = open(fingerprint_path).read()
    data = {"fingerprint": fingerprint,
            "callbackId": CALLBACK_ID}
    msg = "Doing authentication (Url: {ur})".format(ur=IDENTIFY_URL)
    logger.info(msg)
    r = requests.post(IDENTIFY_URL, auth=HTTPBasicAuth(token, ''),
                      headers=headers, data=json.dumps(data))
    msg = "{code} -> {content}".format(code=r.status_code, content=r.content)
else:
    msg = "Finished with code {code}, couldn't do auth"\
        .format(code=r.status_code)
logger.info(msg)
