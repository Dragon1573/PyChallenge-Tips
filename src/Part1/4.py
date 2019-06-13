"""
@Name: 4.py

@Author: Drogon1573
@Date: 2019/6/12 11:57 CST
"""
from requests import get
from re import search

if __name__ == "__main__":
    # 设置初始页面
    page_id = "12345"
    # 设置页面前缀
    PREFIX = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    while True:
        web_page = get(PREFIX + page_id)
        print(web_page.text)
        try:
            page_id = search(
                r"nothing is ([0-9]+)",
                web_page.text
            ).group(1)
        # 处理特殊情况
        except AttributeError:
            if search(r"Yes", web_page.text):
                page_id = str(int(page_id) // 2)
            else:
                break
