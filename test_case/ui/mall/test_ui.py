from selenium import webdriver

# 项目根目录建config包，里面建conf.py文件，用于配置
from config import conf


# 项目根目录建config包，里面建conf.py文件，用于配置
from config import conf
from config.conf import DRIVER_PATH, url
from tool.base_ui import BaseUI
dr = webdriver.Chrome(DRIVER_PATH)
dr.maximize_window()  # 最大化浏览器
dr.implicitly_wait(8)  # 设置隐式时间等待
# 使用baseUI
base = BaseUI(dr)



# https://github.com/LudvikWoo/guoya-pycharm-settings.git