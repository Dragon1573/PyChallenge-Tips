"""
@Name: 13.py

@Author: Drogon1573
@Date: 2019/6/13 16:50 CST
"""
from xmlrpc import client as mobile

if __name__ == "__main__":
    # 连接运营商
    isp = mobile.Server("http://www.pythonchallenge.com/pc/phonebook.php")
    # 调用phone()函数进行呼叫
    print(isp.phone("Bert"))
