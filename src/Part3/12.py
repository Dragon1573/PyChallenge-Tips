"""
@Name: 12.py

@Author: Drogon1573
@Date: 2019/6/13 15:04 CST
"""
if __name__ == "__main__":
    # 读取数据
    with open("resources/evil2.gfx", "rb") as target:
        content = target.read()

    # 测试发现，分组后的5个二进制文件各自形成一张图片
    # 所以使用图片的格式进行存储。
    for k in range(5):
        with open("resources/answer%d.jpg" % k, "wb") as target:
            target.write(content[k::5])
