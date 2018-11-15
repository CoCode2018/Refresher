"""
variables
    n.可变因素，变数( variable的名词复数 )
nothing more than
    仅仅、只不过
lousy
    adj.讨厌的;污秽的;多虱的;不清洁的
memories
    n.记忆力( memory的名词复数 );记忆中的事物;记忆系统;记忆容量
they'd == they had
    他们会、他们过去曾经
they'd == they would
    他们愿意
stuck
    v.刺(stick 的过去式及过去分词)
    adj.动不了的;被卡住的;被…缠住的;被…难住的，不知所措
taught
    v.教育;教( teach的过去式和过去分词 );教书;训练
carpool
    v.拼车;合伙使用汽车
capacity
    n.容量;性能;才能;生产能力
    adj.充其量的，最大限度的
space
    n.空间，太空;空白，间隔;空隙;片刻
    vt.把…分隔开，留间隔于…之间
    vi.以一定间隔排列
imaginary
    adj.幻;虚幻;想像中的，假想的，虚构的;[数]虚数的
decimal
    adj.十进位的，小数的
    n.小数
assignments
    n.工作;分配( assignment的名词复数 );任命;归属
purpose
    n.目的;意志;作用;（进行中的）行动
    vt.有意;打算;企图（做）;决意（做）
etc.
    adv.<拉>等等，以及其他
underscore
    vt.划线于…下，强调
    n.底线;（表示强调的）下方划线;（影片等的）伴音
mostly
    adv.大部分，多半;主要地;基本上;通常
"""

"""
Write a comment above each line explaining to yourself what it does in English.
Read your .py file backward.
Read your .py file out loud, saying even the characters.
"""

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars availabele.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")
