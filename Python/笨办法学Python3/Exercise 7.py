"""
Exercise 7: More Printing
    1.The purpose is to build up your chops.
    2.Remember that everyone makes mistakes.
    3.Your goal is to find as many different ways to break your code until you get tired or exhaust all possibilities. 

    
try not to
    尽量不要
magicians
    n.术士;巫师;魔术师( magician的名词复数 );施妖术的人
fool
    n.愚人，傻瓜;受骗者;有癖好的人;受愚弄的人
    vt.愚弄，欺骗;浪费，虚度;闹笑话;游手好闲
    vi.欺骗;开玩笑;戏弄
    adj.愚蠢的;傻的
section
    n.部分;节;部件;部门
    vi.切开;切断;做（动物或植物组织）切片;把（精神病患者）正式送入精神病院
    vt.把…切成片（或段）;作…的切片;把…作成截面;制作…的剖面图
explicitly
    adv.明白地，明确地
exhaust
    vt.排出;用尽，耗尽;使精疲力尽;彻底探讨
    vi.排气
    n.排出;（排出的）废气;排气装置
a specific common way
otherwise
    adv.否则;另外;别的方式
    adj.别的，另外的;不同的
    conj.否则，不然
consider
    vt.& vi.考虑;把（某人，某事）看作…，认为（某人，某事）如何;考虑，细想
    vt.考虑;认为;以为;看重
    vi.仔细考虑;深思
nasty
    adj.肮脏的;下流的，令人讨厌的;恶劣的，艰险的;严重的
    n.令人不愉快的事物
strictly
    adv.严格地;完全地
acceptable
    adj.可接受的;合意的;（社会上）认同的;（礼物等）令人满意的
typically
    adv.通常;典型地;代表性地
although
    conj.虽然;尽管;但是;然而
"""

print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10)     # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
# print()中的end参数定义print后的操作，默认换行
print(end1 + end2 + end3 + end4 + end5 + end6)
print(end7 + end8 + end9 + end10 + end11 + end12)

print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12, end = '\n')

print(end1 + end2 + end3 + end4 + end5 + end6, end = '\t')
print(end7 + end8 + end9 + end10 + end11 + end12)
