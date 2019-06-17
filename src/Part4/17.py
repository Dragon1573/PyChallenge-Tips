"""
@Name: 17.py

@Author: Drogon1573
@Date: 2019/6/17 22:27 CST
"""
from requests import get
from re import search
from bz2 import decompress
from urllib.parse import unquote_to_bytes
from xmlrpc import client

# 全局定义 #
PREFIX = "http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing="
busy_nothing = "12345"
cookie_info = str()

# 主函数 #
if __name__ == "__main__":
    """ 获取Cookies内容 """
    try:
        while True:
            # 获取网页对象
            web_page = get(PREFIX + busy_nothing)
            # 获取Cookie内容
            cookie_info += web_page.cookies.get("info")
            # 获取网页源代码
            source_code = web_page.text
            # 搜索其中的链接编码，并不断执行跳转
            busy_nothing = search(
                r"and the next busynothing is (\d+)",
                source_code
            ).group(1)
    except AttributeError:
        # 结束循环
        pass

    """ bz2解压内容 """
    # 解码后的BZ压缩字符串与URL编码相似
    # 其中是有个+的
    # 要使用字符替换将它转换为%20
    # 再使用urllib.parse.unquote_to_bytes
    # 将BZ2字符串转码为字节串
    bytes_info = unquote_to_bytes(cookie_info.replace("+", "%20"))
    print(decompress(bytes_info).decode("UTF-8"))

    """ xmlrpc与父亲通话 """
    ISP = client.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
    print(ISP.phone("Leopold"))
