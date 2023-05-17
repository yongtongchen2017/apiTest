import pytest


# pytest自定义命令hook函数
def pytest_addoption(parser):
    parser.addoption(
        "--baseUrl", action="store", default=None, help="输入你base_url"
    )


# 定义fixture
@pytest.fixture(scope="session")
def base_url(request):
    return request.config.getoption("--baseUrl")
