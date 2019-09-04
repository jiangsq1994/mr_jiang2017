from selenium import webdriver
from tools import request_tool
from tools import assert_tool
from tools import random_tool
from tools import mysql_tool
from tools import excel_tool
from tools import log_tool
from tools import os_tool
from tools import shell_tool
import pytest
import allure
# 项目根目录建config包，里面建conf.py文件，用于配置
from config import conf
from config.conf import DRIVER_PATH, url
from tool.base_ui import BaseUI

dr = webdriver.Chrome(DRIVER_PATH)
dr.maximize_window()  # 最大化浏览器
dr.implicitly_wait(8)  # 设置隐式时间等待
# 使用baseUI
base = BaseUI(dr)



