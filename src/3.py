"""
@Name: 3.py

@Author: Drogon1573
@Date: 2019/6/12 10:57 CST
"""
from requests import get
import re

if __name__ == "__main__":
    web_page = get("http://www.pythonchallenge.com/pc/def/equality.html")
    source_code = "".join(re.findall(r"\S", web_page.text))
    mess = "".join(re.findall(r"<!--(.*)-->", source_code))
    result = "".join(re.findall(r"[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]", mess))
    print(result)
