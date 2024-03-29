
import allure                                                                                                 
import json                                                                                                   
                                                                                                              
                                                                                                              
@allure.epic('一级归类')                                                                                      
@allure.feature('二级归类')                                                                                   
@allure.story('三级归类')                                                                                     
def test_hello_world():                                                                                       
    print('hello world !')                                                                                    
    request = {                                                                                               
        'pwd': 'a123456',                                                                                     
        'userName': '13s32'                                                                                   
    }                                                                                                         
    allure.attach(json.dumps(request,ensure_ascii=False,indent=4), '请求', allure.attachment_type.TEXT)       
                                                                                                              
    response = {                                                                                              
        'code': 2000,                                                                                         
        'message': '登录成功',                                                                                
        'data': {                                                                                             
            'token': 'eyJ0aW1lT3V0IjoxNTYzNDUxMjg4MjY3LCJ1c2VySWQiOjQwMywidXNlck5hbWUiOiIxM3MzMiJ9',          
            'userName': '13s32'                                                                               
        }                                                                                                     
    }                                                                                                         
    allure.attach(json.dumps(response,ensure_ascii=False,indent=4), '响应', allure.attachment_type.TEXT)      
