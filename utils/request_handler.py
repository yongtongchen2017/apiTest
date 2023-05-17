import requests
from requests_toolbelt import MultipartEncoder

from .logger import logger


def request_handler(method: str, url: str, headers: dict, data: dict):
    """
    :param headers: 请求头
    :param method: 方法字符串
    :param url: 请求地址
    :param data: 请求参数
    :return: 返回响应数据
    """
    try:
        method = method.upper()
        if method == "GET" or method == "DELETE":
            return requests.request(method=method, url=url, params=data, verify=False).json()
        elif method == "POST" or method == "PUT":
            if 'form-data' in headers['Content-Type']:
                m = MultipartEncoder(
                    fields=data
                )
                headers['Content-Type'] = m.content_type
                return requests.request(method=method, url=url, headers=headers, data=m, verify=False).json()
            else:
                return requests.request(method=method, url=url, headers=headers, json=data, verify=False).json()
        else:
            logger.info(f" no support{method}")
    except Exception as e:
        raise e
