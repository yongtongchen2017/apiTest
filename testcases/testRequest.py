import requests

import sys

sys.path.append("..")

from utils.request_handler import request_handler
from utils.logger import logger


class TestRequest:

    def test_get(self):
        r = requests.get("http://www.baidu.com")
        logger.info(f"r is: {r}")
        logger.info(f"r.text is: {r.text}")
        logger.info(f"r.status_code is:{r.status_code}")
        logger.info(f"r.content is:{r.content}")

    def test_post(self):
        url = "https://httpbin.org/post"
        payload = dict(key1='value1', key2='value2')
        r = requests.post(url, params=payload)
        logger.info(f"r is: {r}")
        logger.info(f"r.url is:{r.url}")
        logger.info(f"r.text is: {r.text}")
        logger.info(f"r.status_code is:{r.status_code}")
        logger.info(f"r.content is:{r.content}")

    def test_postByRequestHandler(self):
        url = "https://httpbin.org/post"
        payload = dict(key1='value1', key2='value2')
        method = "POST"
        headers = {'Content-Type': "application/json"}
        r = request_handler(method, url, headers, payload)
        logger.info(f"r is: {r}")
        logger.info(f"r.url is: {r['url']}")
        logger.info(f"r.json is: {r['json']}")
        logger.info(f"r.data is:{r['data']}")
