import json
import re

import jsonpath
from domain.data_parser import DataParser
from utils.logger import logger


class ParserData:

    @staticmethod
    def parserData(expectData: dict, response):
        """
        :param expectData: 期望的数据
        :param response: 返回结果
        :return:
        """
        for key, val in expectData.items():
            value = jsonpath.jsonpath(response, val)[0]
            logger.info("key is: " + key + ", val is:" + val + ", value is:" + value)
            setattr(DataParser, key, str(value))

    @staticmethod
    def get_value(name):
        """
        :param name: 变量名
        :return:
        """
        return getattr(DataParser, name, None)

    @staticmethod
    def handler_request_data(request_data: dict):
        """
        :param request_data: 请求的参数
        :return: 返回的参数
        """
        request_data = json.dumps(request_data)
        regex = r"\$\{.+?\}"
        regex_obj = re.compile(regex)
        replace_values = regex_obj.findall(request_data)
        for val in replace_values:
            key = val[2:-1]
            request_data = request_data.replace(val, getattr(DataParser, key))
        return  json.loads(request_data)

