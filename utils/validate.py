import jsonpath
from hamcrest import *
from .logger import logger


###校验器
class Validate:

    @staticmethod
    def validate(validate_list: list, response):
        for validate in validate_list:
            for key, item in validate.items():
                for key_json_path, item_expect in item.items():
                    logger.info(f"预期结果值是{item_expect}")
                    actual_val = jsonpath.jsonpath(response, key_json_path)[0]
                    logger.info(f"获取真实值是{actual_val}")
                    if key == "equal_to":
                        assert_that(actual_val, equal_to(item_expect))
                    elif key == "greater_than":
                        assert_that(actual_val, greater_than(item_expect))
                    elif key == "less_than":
                        assert_that(actual_val, less_than(item_expect))
                    elif key == "has_length":
                        assert_that(actual_val, has_length(item_expect))
                    elif key == "has_string":
                        assert_that(actual_val, has_string(item_expect))
                    elif key == "greater_than_or_equal_to":
                        assert_that(actual_val, greater_than_or_equal_to(item_expect))
                    elif key == "less_than_or_equal_to":
                        assert_that(actual_val, less_than_or_equal_to(item_expect))
                    else:
                        logger.info("-------暂时不支持该断言方法---------")
