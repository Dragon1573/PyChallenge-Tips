"""
@Name: 11.py

@Author: Drogon1573
@Date: 2019/6/13 13:01 CST
"""
from PIL import Image
from PIL.Image import Image as img

if __name__ == "__main__":
    raw_image: img = Image.open("resources/cave.jpg")
    new_size = tuple(k // 2 for k in raw_image.size)
    odd_image: img = Image.new("RGBA", new_size)
    even_image: img = Image.new("RGBA", new_size)

    # 提取像素
    for x in range(raw_image.size[0]):
        for y in range(raw_image.size[1]):
            if (x + y) % 2 == 0:
                even_image.putpixel(
                    (x // 2, y // 2),
                    raw_image.getpixel((x, y))
                )
            else:
                odd_image.putpixel(
                    (x // 2, y // 2),
                    raw_image.getpixel((x, y))
                )

    # 亮度提升
    odd_image.point(lambda x: x + 100)
    even_image.point(lambda x: x + 100)

    # 显示图片
    odd_image.show("Odd")
    even_image.show("Even")
