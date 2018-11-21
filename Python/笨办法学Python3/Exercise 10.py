"""
Exercise 10: What Was That?
    1.

threw
    v.扔;抛;掷;投( throw的过去式 )
toes
    n.脚趾;脚趾( toe的名词复数 );（鞋，袜的）足尖部;脚趾状物
multiple
    adj.多重的;多个的;复杂的;多功能的
    n.<数>倍数;[电工学]并联;连锁商店;下有多个分社的旅行社
backslash
    n.反斜线符号
various
    adj.各种各样的;多方面的;许多的;各个的，个别的
available
    adj.可获得的;有空的;可购得的;能找到的
Imagine
    想象
actually
    adv.实际上;确实;竟;事实上
spacing
    n.间隔，间距;跨距;疏密;留间隔
memorize
    vt.记住，熟记;[计算机科学] 存储，记忆
Combine
    v.使结合;使化合;兼有;用联合收割机收割
    n.联合;联合收割机;联合集团;组合艺术品（由画，拼贴和构成派雕塑等拼凑而成的艺术品）
Periodically
    adv.周期性地;定期地，偶尔
intentionally
    adv.有意地，故意地
entirely
    adv.完全地;完整地;全部地;彻底地
"""

# escape sequences
tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

fat_cat1 = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(fat_cat1)

# 跨行：使用转义字符    或者使用triple-quotes/triple-simple-quotes
write1 = "I \"understand\" joe."
write2 = "I am 6'2\" tall."
write3 = 'I ma 6\'2" tall.'
