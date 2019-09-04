import pytest
from selenium import webdriver

from config.conf import DRIVER_PATH
from tool.base_ui import BaseUI
# @pytest.fixture(scope="session")
# def base():
#     #fixture装饰器可以设置前置后置步骤
#     #返回值存到了方法名中
#     #测试用例中，根据方法名来使用该方法的返回值
#     # 打开浏览器
#     dr = webdriver.Chrome(DRIVER_PATH)
#     dr.maximize_window()  # 最大化浏览器
#     dr.implicitly_wait(8)  # 设置隐式时间等待
#     # 使用baseUI
#     base = BaseUI(dr)
#     yield base
#     dr.quit()
