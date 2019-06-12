# The Python Challenge 通关教程（转载）
<!-- TOC -->

- [The Python Challenge 通关教程（转载）](#the-python-challenge-通关教程转载)
   - [关于 The Python Challenge](#关于-the-python-challenge)
   - [关于攻略](#关于攻略)
   - [通关教程](#通关教程)
      - [第0关 - 热身](#第0关---热身)
      - [第1关 - 那么，字符替换如何？](#第1关---那么字符替换如何)
      - [第2关 - 光学字符识别](#第2关---光学字符识别)
      - [第3关 - 正则表达式](#第3关---正则表达式)
      - [第4关 - 追随重定向链](#第4关---追随重定向链)
      - [第5关 - 山峰　地狱](#第5关---山峰　地狱)
      - [第6关 - 现在，它们是成对的](#第6关---现在它们是成对的)
      - [第7关 - 自作聪明](#第7关---自作聪明)
      - [第8关 - 很勤劳吗？](#第8关---很勤劳吗)

<!-- /TOC -->

## 关于 The Python Challenge

&emsp;&emsp;[The Python Challenge](http://www.pythonchallenge.com/)是一个闯关游戏，每一关都需要一点[Python](http://www.python.org/)技巧。这个闯关游戏是由[Nadav Samet](http://www.thesamet.com/)制作的。

&emsp;&emsp;所有的关卡都能通过直接、简短（第32关除外）的脚本解决。

&emsp;&emsp;The Python Challenge欢迎任何编程语言的开发者，你可以使用任何编程语言解决大多数关卡，但有那么一些还是需要Python。有时候你需要使用额外的第三方模块，所有的第三方模块都可以从互联网免费下载（`pip`或`conda`）。

&emsp;&emsp;这个游戏只是为了娱乐，没有完结彩蛋等着你。请保留好你编写的脚本文件，它们可能十分重要。

## 关于攻略

&emsp;&emsp;每当你成功地闯过一个关卡，你都会解锁前一关卡的官方攻略（将链接中的`pc`替换为`pcc`）。官方攻略除了最简便、最常用的Python脚本外，还有其他大佬的取巧方法，甚至是其他语言的通关脚本。但**请注意，你是无法查阅尚未通过的关卡攻略的**。

&emsp;&emsp;在开始的几个关卡的右下角都有“一般提示”：

> - 使用提示！它们在绝大多数时候非常有用。
>
> - 研究关卡提供给你的数据。
>
> - **不要去查找攻略！**（(￣_￣|||)既然你都已经来了，那就当它是放屁吧……）

&emsp;&emsp;本攻略整理自国内各大代码社区或论坛，并可能在那些代码的基础上进行修改。其中，[《一个古老的编程游戏：Python Challenge全通攻略》](https://www.cnblogs.com/jimnox/archive/2009/12/08/tips-to-python-challenge.html)是本文攻略部分的主要来源。

&emsp;&emsp;以下是仓库中各文件或脚本的信息：

- 行尾模式：Windows（CRLF，即`\r\n`）
- 文件编码：UTF-8（`chcp 65001`）
- 运行环境：Python Intepreter 3.7.3 64-bit with Anaconda3

## 通关教程

### 第0关 - 热身

[**跳转到关卡**](http://www.pythonchallenge.com/pc/def/0.html)

&emsp;&emsp;使用[脚本](src/0.py)计算图片所示的表达式，得到
$$ \huge 2^{38} = 274,877,906,944 $$

&emsp;&emsp;下方的黄色内容为（已翻译，下同）：

> 提示：尝试替换URL链接地址

&emsp;&emsp;将链接替换为`274877906944.html`，进入下一关。

### 第1关 - 那么，字符替换如何？

[**跳转到关卡**](http://www.pythonchallenge.com/pc/def/274877906944.html)

&emsp;&emsp;图片给出的是一张字符映射表，其映射逻辑是将每个字母按照字母表向后移动2位。第1句金色提示的内容为：

> 所有人在解决这个问题前都会先想2次。

使用[脚本](src/1.py)按照字符映射表替换下方的紫色文本，得到提示：

> 我希望你没有人工地进行翻译，那是计算机做的事。人工翻译是非常低效的，这也是本文段又臭又长地原因，建议使用`string.maketrans()`。现在，对URL链接做相同地处理。

&emsp;&emsp;将链接替换为`ocr.html`，进入下一关。

### 第2关 - 光学字符识别

[**跳转到关卡**](http://www.pythonchallenge.com/pc/def/ocr.html)

&emsp;&emsp;图片是一本书，即使是借助浏览器放大至$500\\\%$也无法看清书中的字符。

&emsp;&emsp;橙色的提示内容为：

> 辨认字符。它们可能在书中，也**可能**在页面源代码中。

&emsp;&emsp;`Ctrl + U`查看网页源代码，在页面源代码结尾（此处指`</html>`标签）处，有一句提示和一大段的标点符号乱码：

> 找到下方乱码中出现次数最少的字符。

&emsp;&emsp;大致浏览乱码可以发现，乱码的起始字符是`%`，整段乱码的上下有HTML注释标记`<!--`和`-->`包围。这将在后面的正则表达式中起到关键作用。

&emsp;&emsp;通过[脚本](src/2.py)爬取网页（乱码太长了，你自己愿意复制并粘贴乱码也是可以的）并按照要求解析乱码，得到数量最少的字符为：`equality`。

&emsp;&emsp;将链接替换为`equality.html`，进入下一关。

### 第3关 - 正则表达式

[**跳转到关卡**](http://www.pythonchallenge.com/pc/def/equality.html)

&emsp;&emsp;这道题目的图片是没有提示作用的。真正的提示是图片下方的金色文本：

> 一个小写字母，两侧都正好有3个大写字母作保镖。

&emsp;&emsp;依旧打开网页源代码，最后也有一段乱码。大致浏览乱码发现其中的乱码只有混合大小写的英文字母。通过[脚本](src/3.py)爬取网页并进行正则表达式匹配，得到指定的内容为`linkedlist`。

&emsp;&emsp;将链接替换为`linkedlist.html`，进入重定向指示页。根据页面提示重定向到`linkedlist.php`，进入下一关。

### 第4关 - 追随重定向链

[**跳转到关卡**](http://www.pythonchallenge.com/pc/def/linkedlist.php)

&emsp;&emsp;题目只有一张图片，点击图片跳转到重定向链头页面`linkedlist.php?nothing=12345`。

&emsp;&emsp;页面内容显示（每次获取关卡得到的重定向链不一定相同）：

> 紧接着，下一个`nothing`的值是44827

按照页面指示多次替换，发现页面存在通用的提示语。

&emsp;&emsp;编写脚本自动破解重定向链，不断跳转后得到一个特殊情况并触发`AttributeError`异常：

```python
from requests import get
from re import search

if __name__ == "__main__":
    # 设置初始页面
    page_id = "12345"
    # 设置页面前缀
    PREFIX = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
    while True:
        web_page = get(PREFIX + page_id)
        print(web_page.text)
        page_id = search(
            r"nothing is ([0-9]+)",
            web_page.text
        ).group(1)
```

> 是的！除以2并继续。

&emsp;&emsp;改进[脚本](src/4.py)，借助`try/except`结构处理特殊情况。最终得到下一关的链接为`peak.html`。

### 第5关 - 山峰　地狱

[**跳转到关卡**](http://www.pythonchallenge.com/pc/def/peak.html)

&emsp;&emsp;从这里开始，就需要一些比较特别的知识了。图片是没有提示意义的，页面给出的提示是

> 读一下

多次拼读后，`peak hell`会越来越像Python提供的对象序列化模块`pickle`。

&emsp;&emsp;查看网页源代码，发现HTML标签`<peakhell src="banner.p" />`。使用[脚本](src/5.py)爬取pickle数据包`banner.p`并解包，并根据获得的二维列表绘制字符画。

&emsp;&emsp;字符画的内容是`channel`，将链接替换为`channel.html`，进入下一关。

### 第6关 - 现在，它们是成对的

[**跳转到关卡**](http://www.pythonchallenge.com/pc/def/channel.html)

&emsp;&emsp;图片是一套拉链（`zip`），网页源代码也写着`<html> <!-- <-- zip -->`，这两个提示都告诉我们这一题可能与Zip压缩文件相关。

&emsp;&emsp;将链接替换为`channel.zip`，下载压缩包到本地并解压到`channel/`文件夹。查看`channel/readme.txt`，解题逻辑与第4关相同，从`channel/90052.txt`开始遍历。

```python
from re import search

if __name__ == "__main__":
    file_ID = "90052"

    while True:
        target = open("resources/channel/" + file_ID + ".txt", "r")
        raw_text = target.read()
        target.close()
        print(raw_text)
        try:
            file_ID = search(r"([0-9]+)", raw_text).group(1)
        except AttributeError:
            break
```

&emsp;&emsp;执行脚本，得到新提示：

> 收集注释

`channel.zip`中的每一个文件都附带了注释，改进脚本借助`zipfile`将它们提取出来。

```python
from re import search
import zipfile

if __name__ == "__main__":
    file_ID = "90052"
    zip_file = zipfile.ZipFile("resources/channel.zip")
    comments = list()

    while True:
        comments.append(
            zip_file.getinfo(
                file_ID + ".txt"
            ).comment.decode("UTF-8")
        )
        target = open("resources/channel/" + file_ID + ".txt", "r")
        raw_text = target.read()
        target.close()
        try:
            file_ID = search(r"([0-9]+)", raw_text).group(1)
        except AttributeError:
            break

    print("".join(comments))
```

&emsp;&emsp;执行脚本，得到字符画`HOCKEY`。重定向到`hockey.html`，获得提示：

> 它们在空气中，注意看字母。

&emsp;&emsp;组成字符画的字母是`oxygen`，重定向到`oxygen.html`，进入下一关。

### 第7关 - 自作聪明

[**跳转到关卡**](http://www.pythonchallenge.com/pc/def/oxygen.html)

&emsp;&emsp;~~网页源代码里什么都没有……~~注意观察图片，图片的中间区域有一片黑白的长条，我们需要借助`PIL`模块对图像进行处理。

&emsp;&emsp;下载并打开图片，黑白长条的左上角坐标是$(0, 43)$，右下角坐标是$(607, 51)$。

&emsp;&emsp;执行[脚本](src/7.py)，得到`integrity`，重定向到`integrity.html`，进入下一关。

### 第8关 - 很勤劳吗？

[**跳转到关卡**](http://www.pythonchallenge.com/pc/def/integrity.html)

> 丢失的链接去哪里了？

&emsp;&emsp;看到这个提示，那么通向下一关卡的链接肯定直接存在于网页中，前往源代码。

```html
<map name="notinsect">
  <area shape="poly" coords="179,284,214,311,255,320,281,226,319,224,363,309,33
  9,222,371,225,411,229,404,242,415,252,428,233,428,214,394,207,383,205,390,195
  ,423,192,439,193,442,209,440,215,450,221,457,226,469,202,475,187,494,188,494,
  169,498,147,491,121,477,136,481,96,471,94,458,98,444,91,420,87,405,92,391,88,
  376,82,350,79,330,82,314,85,305,90,299,96,290,103,276,110,262,114,225,123,212
  ,125,185,133,138,144,118,160,97,168,87,176,110,180,145,176,153,176,150,182,13
  7,190,126,194,121,198,126,203,151,205,160,195,168,217,169,234,170,260,174,282
  " href="../return/good.html" />
</map>
```

&emsp;&emsp;这是HTML5引入的区域链接，对应的链接范围是图片中蜜蜂所在的位置。其中的`../return/good.html`是指向下一关卡的链接。点击链接，需要输入用户名与密码进行登录。

```html
<!--
un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07
<\xc9\x14\xe1BA\x06\xbe\x084'
pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\x
e1BBP\x91\xf08'
-->
```

&emsp;&emsp;上面4行信息是源代码提供的、以`bz2`压缩的用户名与密码。通过[脚本](src/8.py)解压，获得用户名`huge`与密码`file`，登录并进入下一题。
