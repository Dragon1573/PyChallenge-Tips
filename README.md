# The Python Challenge 通关教程（转载）
<!-- TOC -->

- [The Python Challenge 通关教程（转载）](#the-python-challenge-%E9%80%9A%E5%85%B3%E6%95%99%E7%A8%8B%E8%BD%AC%E8%BD%BD)
  - [关于 The Python Challenge](#%E5%85%B3%E4%BA%8E-the-python-challenge)
  - [关于攻略](#%E5%85%B3%E4%BA%8E%E6%94%BB%E7%95%A5)
  - [通关教程](#%E9%80%9A%E5%85%B3%E6%95%99%E7%A8%8B)
    - [第0关 - 热身](#%E7%AC%AC0%E5%85%B3---%E7%83%AD%E8%BA%AB)
    - [第1题 - 那么，字符替换如何？](#%E7%AC%AC1%E9%A2%98---%E9%82%A3%E4%B9%88%E5%AD%97%E7%AC%A6%E6%9B%BF%E6%8D%A2%E5%A6%82%E4%BD%95)
    - [第2题 - 光学字符识别](#%E7%AC%AC2%E9%A2%98---%E5%85%89%E5%AD%A6%E5%AD%97%E7%AC%A6%E8%AF%86%E5%88%AB)

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

[**跳转到本题**](http://www.pythonchallenge.com/pc/def/0.html)

&emsp;&emsp;使用[脚本](src/0.py)计算图片所示的表达式，得到
$$ \huge 2^{38} = 274,877,906,944 $$

&emsp;&emsp;下方的黄色内容为（已翻译，下同）：

> 提示：尝试替换URL链接地址

&emsp;&emsp;将链接替换为`274877906944.html`，进入下一关。

### 第1题 - 那么，字符替换如何？

[**跳转到本题**](http://www.pythonchallenge.com/pc/def/274877906944.html)

&emsp;&emsp;图片给出的是一张字符映射表，其映射逻辑是将每个字母按照字母表向后移动2位。第1句金色提示的内容为：

> 所有人在解决这个问题前都会先想2次。

使用[脚本](src/1.py)按照字符映射表替换下方的紫色文本，得到提示：

> 我希望你没有人工地进行翻译，那是计算机做的事。人工翻译是非常低效的，这也是本文段又臭又长地原因，建议使用`string.maketrans()`。现在，对URL链接做相同地处理。

&emsp;&emsp;将链接替换为`ocr.html`，进入下一关。

### 第2题 - 光学字符识别

[**跳转到本题**](http://www.pythonchallenge.com/pc/def/ocr.html)

&emsp;&emsp;图片是一本书，即使是借助浏览器放大至$500\\\%$也无法看清书中的字符。

&emsp;&emsp;橙色的提示内容为：

> 辨认字符。它们可能在书中，也**可能**在页面源代码中。

&emsp;&emsp;`Ctrl + U`查看网页源代码，在页面源代码结尾（此处指`</html>`标签）处，有一句提示和一大段的标点符号乱码：

> 找到下方乱码中出现次数最少的字符。

&emsp;&emsp;通过[脚本](src/2.py)爬取网页（乱码太长了，你自己愿意复制并粘贴乱码也是可以的）并按照要求解析乱码，得到数量最少的字符为：`equality`。

&emsp;&emsp;将链接替换为`equality.html`，进入下一关。
