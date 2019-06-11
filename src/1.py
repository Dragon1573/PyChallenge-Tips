"""
@Name: 1.py

@Author: Drogon1573
@Date: 2019/6/11 19:24 CST
"""

# 取出小写字母
from string import ascii_lowercase as letters

if __name__ == "__main__":
    s = (
        """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc"""
        """ dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr"""
        """ gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. """
        """lmu ynnjw ml rfc spj."""
    )
    # 将字母表整体后移2位，拼接为新的字母表
    decodeStr = letters[2:] + letters[:2]
    transTable = str.maketrans(letters, decodeStr)
    print(s.translate(transTable))
