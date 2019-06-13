"""
@Name: 16.py

@Author: Drogon1573
@Date: 2019/6/14 1:42 CST
"""
from PIL import Image
from PIL.Image import Image as img

if __name__ == "__main__":
    raw_image: img = Image.open("../resources/mozart.gif")
    new_image: img = Image.new(raw_image.mode, raw_image.size, None)

    for y in range(raw_image.size[1]):
        # 获取每一行的像素
        row = [raw_image.getpixel((x, y)) for x in range(raw_image.size[0])]
        # 紫色像素色彩值为195，每行有4个像素，匹配每行第1个紫色像素即可
        seperator = row.index(195)
        # 调换选区顺序
        row = row[seperator:] + row[:seperator]
        # 将每一行的像素插入新图片中
        for x in range(raw_image.size[0]):
            new_image.putpixel((x, y), row[x])

    # 显示图像
    new_image.show()
