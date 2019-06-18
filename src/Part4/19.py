"""
@Name: 19.py

@Author: Drogon1573
@Date: 2019/6/18 12:45 CST
"""
import re
from urllib.parse import unquote_to_bytes
from base64 import decodebytes
import wave

if __name__ == "__main__":
    # 获取页面源代码
    with open("../resources/please!.html") as file:
        source_code = "".join([
            line for line in file
        ])

    # 去除源代码中的空白字符
    trimed_source = "".join(re.findall(r"\S", source_code))

    # 提取附件内容
    b64_audio = re.search(
        r"base64(.*)--===============1295515792==--",
        trimed_source
    ).group(1)

    # 解码为二进制音频数据
    raw_audio = decodebytes(unquote_to_bytes(b64_audio))

    # 写入音频文件
    with open("../resources/indian.wav", "wb") as file:
        file.write(raw_audio)

    raw: wave.Wave_read = wave.open("../resources/indian.wav", "rb")
    new: wave.Wave_write = wave.open("../resources/reverse.wav", "wb")
    # 设置声道数量
    new.setnchannels(raw.getnchannels())
    # 设置采样范围
    new.setsampwidth(raw.getsampwidth())
    # 设置采集率
    new.setframerate(raw.getframerate())
    # *.wav是一种多声道音频文件
    # 所有声道逐帧翻转
    # 并写入新文件
    for k in range(raw.getnframes()):
        new.writeframes(raw.readframes(k)[::-1])
    raw.close()
    new.close()
