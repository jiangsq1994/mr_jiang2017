import os

url = 'https://www.baidu.com/'

GY_DB_URL = {                               
    'host': '',
    'port': 3306,
    'db': '',
    'user': '',
    'passwd': '',
    'charset': 'utf8'
}											
#设置driver的绝对路径
DRIVER_PATH = os.path.join(os.path.dirname(__file__), "../chrome_driver_v75/chromedriver.exe")