"""
@Name: 18.py

@Author: Drogon1573
@Date: 2019/6/18 9:22 CST
"""
from difflib import Differ

content = (list(), list())

if __name__ == "__main__":
    # 读取文件并拆分
    with open("../resources/delta.txt") as file:
        for line in file:
            parts = line.split("   ")
            content[0].append(parts[0] + "\n")
            content[1].append(parts[1])

    # 对比文件
    compare = Differ().compare(content[0], content[1])

    # 写入文件
    file1 = open("../resources/pic1.png", "wb")
    file2 = open("../resources/pic2.png", "wb")
    file3 = open("../resources/pic3.png", "wb")
    for line in compare:
        byte_str = bytes(
            [
                # 将十六进制字符串转换为数值
                int(i, 16)
                # 将每一行首尾的空白字符去除
                # 并以空格进行拆分
                for i in line[2:].strip().split(" ")
                # 判断数值是否为空
                if i
            ]
        )
        if line[0] == "+":
            file1.write(byte_str)
        elif line[0] == "-":
            file2.write(byte_str)
        else:
            file3.write(byte_str)
    file1.close()
    file2.close()
    file3.close()
