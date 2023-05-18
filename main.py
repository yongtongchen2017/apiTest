# This is a sample Python script.
import os

import pytest
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, utils windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pytest.main(['-vs', '--alluredir=./temp', '--baseUrl=https://api2.mubu.com'])
    os.system(r"rm -rf ./allure-report")
    os.system(r"allure generate ./temp -o ./allure-report --clean")
    os.system(r"allure open ./allure-report")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
