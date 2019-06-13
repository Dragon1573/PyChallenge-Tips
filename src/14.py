"""
@Name: 14.py

@Author: Drogon1573
@Date: 2019/6/13 17:51 CST
"""
from PIL import Image
from PIL.Image import Image as img

if __name__ == "__main__":
    picture: img = Image.open("resources/wire.png")
    result = Image.new(picture.mode, (100, 100))

    # 缠绕方向
    direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # 绕线起点
    x, y = -1, 0
    # 线定位标记
    k = 0
    # 步长（用于匹配绕线规律）
    steps = 200

    # 只要还有步长，图就没有绕完
    while steps / 2 > 0:
        # 四个方向绕一圈
        for vector in direction:
            # 整除以获得实际步长（这下就和绕线规律一样了）
            step = steps // 2
            for i in range(step):
                # 沿着方向前进
                x = x + vector[0]
                y = y + vector[1]
                # 获取线上的像素点
                pixel = picture.getpixel((k, 0))
                # 将像素点放置到图片上
                result.putpixel((x, y), pixel)
                k += 1
            steps -= 1

    # 像素线已经缠绕成图片了，奇迹显现吧！
    result.show()
    result.close()
