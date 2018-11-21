# -*- encoding: UTF-8 -*-

"""
Exercise 9: Printing, Printing, Printing
    1.

realize
    vt.实现;了解，意识到;（所担心的事）发生;以…价格卖出
    vt.& vi.变卖，赚得
pattern
    n.模式;图案;花样，样品;榜样，典范
    vt.模仿;以图案装饰
    vi.形成图案
more than
    超过;不只是;很;在…次以上
concept
    n.观念，概念;观点;思想，设想，想法;总的印象
later
    adv.后来;随后;较晚地;以后，过后
    adj.以后的;后来的;接近末期的;晚年的
stuff
    n.材料，原料，资料;〈俚〉钱，现金;填充物;素材资料
    vt.塞满;填塞;让吃饱
    vi.吃得过多
escape sequence
    转义序列
"""

# Here's some new strange stuff, remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\n"
months2 = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\n"

print("Here are the days: ", days)
print("Here are the months: ", months)
print("Here are the months2: ", months2)

# 尾部的 """ 如果另起一行会输出一个空行
print("""
(Start)There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.(End)""")

print("""
(Start)There's something going on here.
With the three double-qutos.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or6.(End)
""")

# 第一行 """ 之后如果不写东西会输出一个空行
# 其余的字符完全按照书写的格式，输出出来
print("""
    (Start)There's something going on here.
    With the three double-quotes.
    We'll be able to type as much as we like.
    Even 4 lines if we want, or 5, or 6.(End)
    """)

print("""(Start)There's something going on here.
With the three double-quotes.
    We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.(End)""")

print("End....")
print("""End....""")
print("""
End\n""")

# video

# escape sequence(转义序列)
# 如果我们要使用特殊符号，例如引号中的引号，需要使用转义字符
# 当Python遇到 \ 时，判断是否是特殊字符、普通字符
#   如果是特殊字符:     \n, 特殊输出
#   如果不是特殊字符:   \", 打印字符
moths3 = "Jan\nFeb\nMar\"\nApr\nMay\nJun\nJul\nAug\n"

# 三个双引号字符串
# 里面可以嵌套其他任意的引号会原样输出
# 三引号开头如果是空行会输出一个空行
# 三引号结尾如果是新行也会输出一个空行
# 三引号里面的转义序列仍然有效果