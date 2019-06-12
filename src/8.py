"""
@Name: 8.py

@Author: Drogon1573
@Date: 2019/6/12 20:37 CST
"""
from bz2 import decompress

if __name__ == "__main__":
    username = b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
    password = b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"
    print("Username:", decompress(username).decode("UTF-8"))
    print("Password:", decompress(password).decode("UTF-8"))
