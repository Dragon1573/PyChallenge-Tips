"""
@Name: 5.py

@Author: Drogon1573
@Date: 2019/6/12 13:36 CST

@Comments:
    这个脚本通过requests直接从网页爬取数据，
    您不需要再额外下载数据文件。
"""
from requests import get
from pickle import loads

if __name__ == "__main__":
    # 爬取pickle数据包
    web_page = get("http://www.pythonchallenge.com/pc/def/banner.p")
    # 载入数据
    data = loads(web_page.content)
    # 绘制字符画
    # 很多教程在此处使用的是列表生成式
    # 但列表生成式不适合多重嵌套
    # 嵌套层数过高反而会让代码可读性下降
    for line in data:
        for item in line:
            # 每个item有2个数据：
            # 字符及其重复次数
            # 输出时不能添加分隔号与换行
            print(item[0] * item[1], sep="", end="")
        # 数据的每一个元素还是列表
        # 代表完整的一行
        # 不换行将导致字符画排版错误
        print()
