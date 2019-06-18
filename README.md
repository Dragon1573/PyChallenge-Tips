# The Python Challenge 通关教程（转载）

<!-- TOC -->

- [关于 The Python Challenge](#关于-The-Python-Challenge)
- [关于攻略](#关于攻略)
- [通关教程](#通关教程)
  - [第0关 - 热身](#第0关---热身)
  - [第1关 - 那么，字符替换如何](#第1关---那么字符替换如何)
  - [第2关 - 光学字符识别](#第2关---光学字符识别)
  - [第3关 - 正则表达式](#第3关---正则表达式)
  - [第4关 - 追随重定向链](#第4关---追随重定向链)
  - [第5关 - 山峰 地狱](#第5关---山峰地狱)
  - [第6关 - 现在，它们是成对的](#第6关---现在它们是成对的)
  - [第7关 - 自作聪明](#第7关---自作聪明)
  - [第8关 - 很勤劳吗](#第8关---很勤劳吗)
  - [第9关 - 连点成线](#第9关---连点成线)
  - [第10关 - 你在看什么](#第10关---你在看什么)
  - [第11关 - 奇数 偶数](#第11关---奇数偶数)
  - [第12关 - 解决恶魔](#第12关---解决恶魔)
  - [第13关 - 打电话给他](#第13关---打电话给他)
  - [第14关 - 绕圈圈](#第14关---绕圈圈)
  - [第15关 - 谁](#第15关---谁)
  - [第16关 - 让我把它变直](#第16关---让我把它变直)
  - [第17关 - 吃](#第17关---吃)
  - [第17.5关 - 是我，你想要什么](#第175关---是我你想要什么)
  - [第18关 - 你能说出差别吗](#第18关---你能说出差别吗)
  - [第19关 - 请](#第19关---请)

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

&emsp;&emsp;使用[脚本](src/Part1/0.py)计算图片所示的表达式，得到
$$ \huge 2^{38} = 274,877,906,944 $$

&emsp;&emsp;下方的黄色内容为（已翻译，下同）：

> 提示：尝试替换URL链接地址

&emsp;&emsp;将链接替换为`274877906944.html`，进入下一关。

### 第1关 - 那么，字符替换如何

[**跳转到关卡**](http://www.pythonchallenge.com/pc/def/274877906944.html)

&emsp;&emsp;图片给出的是一张字符映射表，其映射逻辑是将每个字母按照字母表向后移动2位。第1句金色提示的内容为：

> 所有人在解决这个问题前都会先想2次。

使用[脚本](src/Part1/1.py)按照字符映射表替换下方的紫色文本，得到提示：

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

&emsp;&emsp;通过[脚本](src/Part1/2.py)爬取网页（乱码太长了，你自己愿意复制并粘贴乱码也是可以的）并按照要求解析乱码，得到数量最少的字符为：`equality`。

&emsp;&emsp;将链接替换为`equality.html`，进入下一关。

### 第3关 - 正则表达式

[**跳转到关卡**](http://www.pythonchallenge.com/pc/def/equality.html)

&emsp;&emsp;这道题目的图片是没有提示作用的。真正的提示是图片下方的金色文本：

> 一个小写字母，两侧都正好有3个大写字母作保镖。

&emsp;&emsp;依旧打开网页源代码，最后也有一段乱码。大致浏览乱码发现其中的乱码只有混合大小写的英文字母。通过[脚本](src/Part1/3.py)爬取网页并进行正则表达式匹配，得到指定的内容为`linkedlist`。

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

&emsp;&emsp;改进[脚本](src/Part1/4.py)，借助`try/except`结构处理特殊情况。最终得到下一关的链接为`peak.html`。

### 第5关 - 山峰&emsp;地狱

[**跳转到关卡**](http://www.pythonchallenge.com/pc/def/peak.html)

&emsp;&emsp;从这里开始，就需要一些比较特别的知识了。图片是没有提示意义的，页面给出的提示是

> 读一下

多次拼读后，`peak hell`会越来越像Python提供的对象序列化模块`pickle`。

&emsp;&emsp;查看网页源代码，发现HTML标签`<peakhell src="banner.p" />`。使用[脚本](src/Part2/5.py)爬取pickle数据包`banner.p`并解包，并根据获得的二维列表绘制字符画。

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

&emsp;&emsp;执行[脚本](src/Part2/7.py)，得到`integrity`，重定向到`integrity.html`，进入下一关。

### 第8关 - 很勤劳吗

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

&emsp;&emsp;上面4行信息是源代码提供的、以`bz2`压缩的用户名与密码。通过[脚本](src/Part2/8.py)解压，获得用户名`huge`与密码`file`，登录并进入下一题，后续密码也将使用相同的密码进行登录。

### 第9关 - 连点成线

[**跳转到关卡**](http://www.pythonchallenge.com/pc/return/good.html)

&emsp;&emsp;图片中有一些小黑点，这些点围绕着树木，并没有特别明显的形状，果断查看源代码。

&emsp;&emsp;在源代码中有一大段特殊的注释：

```html
<!--
first+second=?

first:
146,399,163,403,170,393,169,391,166,386,170,381,170,371,170,355,169,346,167,335,
170,329,170,320,170,310,171,301,173,290,178,289,182,287,188,286,190,286,192,291,
194,296,195,305,194,307,191,312,190,316,190,321,192,331,193,338,196,341,197,346,
199,352,198,360,197,366,197,373,196,380,197,383,196,387,192,389,191,392,190,396,
189,400,194,401,201,402,208,403,213,402,216,401,219,397,219,393,216,390,215,385,
215,379,213,373,213,365,212,360,210,353,210,347,212,338,213,329,214,319,215,311,
215,306,216,296,218,290,221,283,225,282,233,284,238,287,243,290,250,291,255,294,
261,293,265,291,271,291,273,289,278,287,279,285,281,280,284,278,284,276,287,277,
289,283,291,286,294,291,296,295,299,300,301,304,304,320,305,327,306,332,307,341,
306,349,303,354,301,364,301,371,297,375,292,384,291,386,302,393,324,391,333,387,
328,375,329,367,329,353,330,341,331,328,336,319,338,310,341,304,341,285,341,278,
343,269,344,262,346,259,346,251,349,259,349,264,349,273,349,280,349,288,349,295,
349,298,354,293,356,286,354,279,352,268,352,257,351,249,350,234,351,211,352,197,
354,185,353,171,351,154,348,147,342,137,339,132,330,122,327,120,314,116,304,117,
293,118,284,118,281,122,275,128,265,129,257,131,244,133,239,134,228,136,221,137,
214,138,209,135,201,132,192,130,184,131,175,129,170,131,159,134,157,134,160,130,
170,125,176,114,176,102,173,103,172,108,171,111,163,115,156,116,149,117,142,116,
136,115,129,115,124,115,120,115,115,117,113,120,109,122,102,122,100,121,95,121,8
9,115,87,110,82,109,84,118,89,123,93,129,100,130,108,132,110,133,110,136,107,138
,105,140,95,138,86,141,79,149,77,155,81,162,90,165,97,167,99,171,109,171,107,161
,111,156,113,170,115,185,118,208,117,223,121,239,128,251,133,259,136,266,139,276
,143,290,148,310,151,332,155,348,156,353,153,366,149,379,147,394,146,399

second:
156,141,165,135,169,131,176,130,187,134,191,140,191,146,186,150,179,155,175,157,
168,157,163,157,159,157,158,164,159,175,159,181,157,191,154,197,153,205,153,210,
152,212,147,215,146,218,143,220,132,220,125,217,119,209,116,196,115,185,114,172,
114,167,112,161,109,165,107,170,99,171,97,167,89,164,81,162,77,155,81,148,87,140
,96,138,105,141,110,136,111,126,113,129,118,117,128,114,137,115,146,114,155,115,
158,121,157,128,156,134,157,136,156,136

-->
```

&emsp;&emsp;按照关卡标题（`connect the dots`）的提示，上面的2组数据是连线所需要的坐标点信息，将2组数据分别绘制的图形拼在一起，得到的整体图案就是下一关的链接地址。

&emsp;&emsp;用[脚本](src/Part2/9.py)绘制图案，得到一头牛。重定向到`cow.html`，得到提示：

> 嗯，它是雄性的。

继续重定向到`bull.html`，进入下一关。

### 第10关 - 你在看什么

[**跳转到关卡**](http://www.pythonchallenge.com/pc/return/bull.html)

&emsp;&emsp;题目的图片是我们上一题线条画的原图，下方的提示询问我们
$$ \large len(a[30])=\\\;? $$

&emsp;&emsp;既然`a`是一个序列，那么a在哪？根据网页标签的提示，点击站立的牛（我们上一题画图的区域），重定向到`sequence.txt`。

$$ \large a=[1, 11, 21, 1211, 111221, \dotsb $$

&emsp;&emsp;列表的开头是`1`，随后是1个`1`、2个`1`、1个`2`加1个`1`、1个`1`加1个`2`加2个`1`。按照规律，每一项的长度将会呈现爆炸式增长。

&emsp;&emsp;编写[脚本](src/Part3/10.py)以获得第30项的长度（**注意：此处使用数组下标来标记项，1是第0项**），运行得到结果
$$ \large len(a[30])=5808 $$
跳转到`5808.html`，进入下一关。

### 第11关 - 奇数&emsp;偶数

[**跳转到关卡**](http://www.pythonchallenge.com/pc/return/5808.html)

&emsp;&emsp;题目的图片是由2张图片、分别提取奇数像素和偶数像素叠加形成的，将图片放大，也能在图片上发现黑色的斜向网格。我们发现，黑色像素点（斜向网格）位于（图片左上角为原点向下、向右拓展）横纵坐标总和为偶数的点上，彩色像素点（我们能看到的模糊图案）位于横纵坐标总和为奇数的点。

&emsp;&emsp;运行[脚本](src/Part3/11.py)，用`PIL`模块将2张图片的像素点分离。在显示出的黑色背景图片的右上角写有淡淡的`evil`字样，访问`evil.html`进入下一关。

### 第12关 - 解决恶魔

[**跳转到关卡**](http://www.pythonchallenge.com/pc/return/evil.html)

&emsp;&emsp;题目的图片是一个人在向5个牌组发牌。查看网页源代码，显示题目图片为`evil1.jpg`，点击链接，正是我们刚才看到的图片。

&emsp;&emsp;尝试访问`evil2.jpg`，图片显示文字为

> 不是jpg，是*.gfx

。访问`evil3.jpg`，提示：

> 没有更多的恶魔了

。访问`evil4.jpg`（**只能在Internet Explorer正常显示**），显示一个网页：

> Bert是恶魔！回去！

访问`evil2.gfx`，下载文件。

&emsp;&emsp;`*.gfx`文件是一种二进制文件。把`evil2.gfx`作为一个“牌堆”，按顺序将其中的“牌”（每一个字节）分发到5个“牌组”（文件）里。分组结果表名，得到的5个文件都是图像，所以使用`*.jpg`作为后缀名。

&emsp;&emsp;运行[脚本](src/Part3/12.py)，得到5张图片，内容分别是`dis`、`pro`、`port`、`ional`、~~`ity`~~（**图五的3个字母被划去**），所以答案为`disproportial`。访问`disproportional.html`进入下一关。

### 第13关 - 打电话给他

[**跳转到关卡**](http://www.pythonchallenge.com/pc/return/disproportional.html)

&emsp;&emsp;图片是一个固定电话的键盘，金色提示语说：

> 给恶魔打电话

那么，“他”是谁？谁才是恶魔？

&emsp;&emsp;还记得上一题的`evil4.jpg`吗？那就打电话给Bert吧，不过要怎么打电话？

&emsp;&emsp;点击键盘5号键，会打开`../phonebook.php`，内容是一个没有与任何自定义标签表关联的XML文件。Python中有一个叫做`xmlrpc.client`的模块，它能利用HTTP协议、将RPC封包编码为XML文件以传输复杂数据，并实现远程对象调用。有没有可能是使用这个包来“打电话”呢？

&emsp;&emsp;编写并运行[脚本](src/Part3/13.py)，Bert给我们的回复是

> 555-ITALY

访问`italy.html`进入下一关。

### 第14关 - 绕圈圈

[**跳转到关卡**](http://www.pythonchallenge.com/pc/return/italy.html)

&emsp;&emsp;上方的大图片是一块螺旋形的大面包，而下面还有一个小图片。在新窗口打开小图片，图片名为`wire.png`（线？？？），大小为 $10000\times1$ 。查看网页源代码，其中的注释如下：

```html
<!-- remember: 100*100 = (100+99+99+98) + (...  -->
```

&emsp;&emsp;注释告诉我们，`wire.png`应该是一张 $100\times100$ 的方形图片，像上面的大面包那样从外向内顺时针缠绕起来，每一组括号都是一个完整的像素环，依照规律就能还原最初的图像。

&emsp;&emsp;编写并运行[脚本](src/Part3/14.py)，显示的结果图像是一只猫。访问`cat.html`，出现了一张完整清晰的图片，上面有2只猫，金色提示写着：

> 它的名字叫**uzi**，你后续会了解他的。

重定向到`uzi.html`，进入下一关。

### 第15关 - 谁

[**跳转到关卡**](http://www.pythonchallenge.com/pc/return/uzi.html)

&emsp;&emsp;图片是一张日历，日历的月份是1月，年份是1??6年，中间的2位被涂黑了，下面的1月26日被画上了一个圈。查看源代码，2个注释起到了关键的提示作用：

```html
<!-- he ain't the youngest, he is the second -->
<!-- todo: buy flowers for tomorrow -->
```

&emsp;&emsp;注释给了我们2个信息：

- 他不是最小的，他是第2小的
- 待办事项：为明天买花

&emsp;&emsp;日期已经确定了，那么年份呢？将网页放大到$500\\\%$，隐约在右下角的2个小日历里发现当年的2月是有29天的。好的，在1006～1996年中寻找满足以下条件的年份：

- 当年是闰年
- 当年的1月27日是星期二
- 当年是满足以上2个条件中第2大的

&emsp;&emsp;编写并运行[脚本](src/Part4/15.py)，求得年份为1756年。[查阅资料](https://baike.baidu.com/item/%E6%B2%83%E5%B0%94%E5%A4%AB%E5%86%88%C2%B7%E9%98%BF%E7%8E%9B%E5%A4%9A%E4%BC%8A%E6%96%AF%C2%B7%E8%8E%AB%E6%89%8E%E7%89%B9/6129936?fromtitle=%E8%8E%AB%E6%89%8E%E7%89%B9&fromid=159018)得知，当天是莫扎特（**Mozart**）的生日。访问`mozart.html`进入下一关。

### 第16关 - 让我把它变直

- [**跳转到关卡**](http://www.pythonchallenge.com/pc/return/mozart.html)
- [脚本](src/Part4/17.py)

&emsp;&emsp;题目有一张雪花状的图片，上面存在大量的粉红色短线条。按照页面标题的指引，应该是使用图像处理把它们变直~~（源代码我看过了，什么也线索没有）~~。

&emsp;&emsp;下载题目的图片`mozart.gif`，编写并运行[脚本](src/Part4/16.py)，获得图片（处理后的图片失去了其应有的色彩，但不影响效果）的内容是`romance`。访问`romance.html`进入下一关。

### 第17关 - 吃

[**跳转到关卡**](http://www.pythonchallenge.com/pc/return/romance.html)

&emsp;&emsp;题目的图片由2幅图片拼合而成，大图片是一些**曲奇饼干（Cookies）**，而左下角的图片正好在第4题也出现过。

&emsp;&emsp;根据图片和网页标题的提示，我们需要在浏览器的缓存（Cookies）中进一步寻找线索。在浏览器（我用的是Google Chrome）中看到其中一个Cookie的内容是~~（注：此处我由于无法获取Cookie差点卡关了）~~：

> 你需要跟着`busynothing`

&emsp;&emsp;结合左下角那张第4题的图片，我们应该需要从`http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345`开始按照跳转顺序获取Cookie的内容。

&emsp;&emsp;编写并运行脚本，得到一串以`BZ`开头的`bz2`压缩字符串：

> BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0+%00hE%3DM%B5%23%D0%
> D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E
> 8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86
> %05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90

&emsp;&emsp;改进脚本，将压缩字符串中的`+`替换为`%20`，借助`urllib.parse.unquote_to_bytes`函数转换为字节串再提供给`bz2.decompress`函数解压，得到：

> 已经26日了？打电话给他的父亲并告知他“花已经在路上了”，他会明白的。

&emsp;&emsp;又是“打电话”？还是用回第13题的方法，打电话给列奥波尔得·莫扎特（**Leopold** Mozart，沃尔夫冈·阿玛多伊斯·莫扎特的父亲，~~奥地利宫廷乐师、作曲家、小提琴家~~），并将信息作为Cookie附加在请求中，得到回复：

> 555-VIOLIN

&emsp;&emsp;前往`violin.html`，进入中间关卡。

### 第17.5关 - 是我，你想要什么

[**跳转到关卡**](http://www.pythonchallenge.com/pc/stuff/violin.php)

&emsp;&emsp;现在，我们联系上列奥波尔得了。在Chrome的开发者工具中，前往`Application -> Storage -> Cookies -> http://www.pythonchallenge.com/`，将`Name = info`项的`Value`修改为`the flowers are on their way`，`F5`刷新页面，得到金色提示：

> 好吧，你绝对不能忘了气球（**balloons**）。

&emsp;&emsp;前往`balloons.html`，自动重定向至下一关（`../return/balloons.html`）。

### 第18关 - 你能说出差别吗

[**跳转到关卡**](http://www.pythonchallenge.com/pc/return/balloons.html)

&emsp;&emsp;关卡有2张图片~~其实是拼接起来的完整一大张~~，图片的内容貌似是一样的（都是2只鹅）。查看网页源代码，得到提示：

```html
<!-- it is more obvious that what you might think -->
```

> 他比你想象的明显多了

&emsp;&emsp;不就是亮度的差别吗？~~不需要用Python处理图片~~访问`bright.html`。

> ness

&emsp;&emsp;`ness`？这是什么鬼？单词后缀？尝试访问`brightness.html`，还是刚才的图片。日常看源代码，发现提示：

```html
<!-- maybe consider deltas.gz -->
```

&emsp;&emsp;按照提示下载`deltas.gz`~~（`*.gz`是`gzip`压缩文件）~~，解压后得到`delta.txt`。文件内容分为左右2个部分，以3个空格作为分隔。编写[脚本](src/Part4/18.py)，借助`difflib`库对左右两个部分进行差异比对，并将比对产生的3个部分分别转换为字节串写入图片文件中，得到三张图片，内容分别为：

> `../hex/bin.html` \
> butter \
> fly

&emsp;&emsp;访问`../hex/bin.html`，输入用户名`butter`、密码`fly`，进入下一关。

### 第19关 - 请

- [**跳转到关卡**](http://www.pythonchallenge.com/pc/return/balloons.html)
- [脚本](src/Part4/19.py)

&emsp;&emsp;题目是一张印度地图，查看源代码，下面有一段类似于电子邮件的注释：

```html
<!--
From: leopold.moz@pythonchallenge.com
Subject: what do you mean by "open the attachment?"
Mime-version: 1.0
Content-type: Multipart/mixed; boundary="===============1295515792=="

It is so much easier for you, youngsters.
Maybe my computer is out of order.
I have a real work to do and I must know what's inside!

--===============1295515792==
Content-type: audio/x-wav; name="indian.wav"
Content-transfer-encoding: base64

UklGRvyzAQBXQVZFZm10IBAAAAABAAEAESsAACJWAAACABAAZGF0YdizAQBABkAMQAtAAEADQAJA
...（此处省略）
Bj8HPwdABT8BQApABj8BQA9AAT8IQA0/Dj8EQAk/A0AHQAw/EEAPQAM/AkANPw8/AUAAPwBAB0AA
PwRACEAGPwpADj8JQBA=

--===============1295515792==--

-->
```

> 来自：leopold.moz@pythonchallenge.com \
> 主题：你所说的“打开附件”是什么意思？ \
> Mime版本：1.0 \
> 内容类型：多部份/混合，边界为`===============1295515792==`
>
> 对你来说应该很简单，年轻人。 \
> 也许我的电脑**乱码**了， \
> 我有重要的工作要做，所以我必须要知道它~~此处指附件~~里面是什么。
>
> --===============1295515792== \
> 内容格式：音频/波形；名称：**`indian.wav`** \
> 内容编码格式：**base64**

&emsp;&emsp;从列奥波尔得的邮件中我们知道，附件是一段以`Base64`加密的`indian.wav`音频文件。将附件解码为`indian.wav`。音频中存在单词**`sorry`**，前往`sorry.html`，网页源代码只有一句

> 你为什么要道歉？

&emsp;&emsp;上文提示老列的设备乱码了，尝试对`indian.wav`的所有声道逐帧翻转为`reverse.wav`。播放解码后的`reverse.wav`中有关键词**`idiot`**，访问`idiot.html`，进入过渡页。

&emsp;&emsp;老列明白了附件的内容，

> 现在你该道歉了……

点击金色链接前往下一关。
