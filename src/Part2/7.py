"""
@Name: 7.py

@Author: Drogon1573
@Date: 2019/6/12 18:09 CST
"""
from PIL import Image
import re

if __name__ == "__main__":
    # 类型不是必须的，此处仅用于激活IntelliCode
    picture: Image.Image = Image.open("resources/oxygen.png")
    # 裁剪图片
    myth_rect = picture.crop((0, 43, 607, 51))
    # 将图片转换为灰度模式
    myth_rect = myth_rect.convert("L")
    # 解码得到提示
    hint = "".join(
        # 将像素按ASCII译码为字符
        chr(myth_rect.getpixel((x, 5)))
        # 每7个像素为一组，传递相同的信息
        for x in range(0, 607, 7)
    )
    # 提示给出的下一关地址仍是以ASCII编码的
    # 用正则表达式提取数值并解码
    answer = re.findall(r"([0-9]+)", hint)
    print("".join([chr(int(i)) for i in answer]))
