import pytest

from utils.logger import logger


@pytest.fixture(scope="function", params=["a", "b", "c"])
def my_fixture(request):
    logger.info("this is fixture")
    return request.param


def setup_class():
    logger.info("每个测试类前执行")


def teardown_class():
    logger.info("每个测试类后执行")


def setup_method():
    logger.info("每个用例前执行")


def teardown_method():
    logger.info("每个用例后执行")


class TestPytest:

    @pytest.mark.smoke
    @pytest.mark.run(order=2)
    def test_demo(self):
        a = 1
        b = 1
        assert a == b

    @pytest.mark.run(order=1)
    def test_demo1(self):
        a = 1
        b = 1
        assert a == b

    @pytest.mark.parametrize("parameter", ["a", "b", "c"])
    def test_demo2(self, parameter):
        logger.info(parameter)
        a = 1
        b = 1
        assert a == b
