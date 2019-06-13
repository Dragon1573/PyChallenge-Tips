"""
@Name: 10.py

@Author: Drogon1573
@Date: 2019/6/13 1:42 CST
"""
import re

if __name__ == "__main__":
    # 初始序列
    item = "1"

    # a[1]～a[30]
    for k in range(1, 31):
        # \d匹配单个数字
        # \1表示匹配前一个相同的字符
        # *表示匹配任意数量
        # 这样元素中的重复序列提取出来
        grep_group = re.findall(r"(\d)(\1*)", item)
        item = "".join([
            # 按照规则，描述出现了几次相同的数字
            str(len(k[0] + k[1])) + k[0]
            for k in grep_group
        ])
    # 最后一个序列的长度就是我们所需要的
    print(len(item))
