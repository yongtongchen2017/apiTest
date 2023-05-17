import pytest

import sys

sys.path.append("..")

from utils.request_handler import request_handler
from utils.read_yaml import read_yaml

from utils.logger import logger


class TestYaml:

    @pytest.mark.parametrize("yamlData", read_yaml("test.yml"))
    def testYaml(self, yamlData, base_url: str):
        logger.info(f"data is: {yamlData}")
        testdata = yamlData['testCase']
        # url='https://api2.mubu.com'
        res = request_handler(testdata['method'], base_url + testdata['uri'], testdata['headers'], testdata['payload'])
        logger.info(f"res is: {res}")
        logger.info(f"res.code is:{res['code']}")
        # logger.info(f"res.token is: {res['data']['token']}")
