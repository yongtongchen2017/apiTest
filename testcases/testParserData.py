import pytest

import sys

from utils.validate import Validate

sys.path.append("..")

from utils.request_handler import request_handler
from utils.read_yaml import read_yaml
from utils.logger import logger
from utils.parser_data import ParserData


class TestParserData:

    @pytest.mark.parametrize("yamlData", read_yaml("test.yml"))
    def testRequestData(self, yamlData, base_url):
        logger.info(f"data is: {yamlData}")
        testdata = yamlData['testCase']
        testdata = ParserData.handler_request_data(testdata)
        res = request_handler(testdata['method'], base_url + testdata['uri'], testdata['headers'], testdata['payload'])
        logger.info(f"res is: {res}")
        if 'extract' in testdata:
            ParserData.parserData(testdata['extract'], res)
            logger.info(f"res.token is: {ParserData.get_value('token')}")
        if 'validate' in testdata:
            validate_list = testdata['validate']
            Validate.validate(validate_list, res)