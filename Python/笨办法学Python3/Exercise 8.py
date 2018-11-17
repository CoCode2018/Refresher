"""
Exercise 8: Printing, Printing
    1.That's a lot for the eighth exercise,

complicated
    adj.结构复杂的;混乱的，麻烦的
    v.使复杂化( complicate的过去式)
essential
    adj.必要的;本质的;基本的;精华的
    n.必需品;基本要素;必不可少的东西
representing
    v.代表;体现;表现( represent的现在分词 );作为…的代表
concept
    n.观念，概念;观点;思想，设想，想法;总的印象
brain teaser
    脑筋急转弯，动动脑筋
consider this
    设想一下; 思索一下
alright
    adv.好的;正确;令人满意
    adj.没问题的
the rest of the book
    书的其余部分
going on
    发生;接近，快到
"""

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear",
))