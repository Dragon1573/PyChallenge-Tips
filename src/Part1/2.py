"""
@Name: 2.py

@Author: Drogon1573
@Date: 2019/6/11 20:37 CST
"""

# 爬取网页
from requests import get
# 正则表达式
import re

if __name__ == "__main__":
    # 爬取网页
    webPage = get("http://www.pythonchallenge.com/pc/def/ocr.html")
    # 获取网页源代码
    sourceCode = webPage.text
    # 去除空白字符
    trimed = "".join(re.findall(r"\S", sourceCode))
    # 提取乱码
    mess: str = re.search(r"<!--(%.*)-->", trimed).group(1)
    # 提取乱码中的英文字符
    result = "".join(re.findall(r"[a-zA-Z]", mess))
    print(result)
