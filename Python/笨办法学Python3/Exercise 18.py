"""
Exercise 18: Names, Variables, Code, Functions
    1.Every programmer will go on and on about functions

introduce
    vt.介绍;引进;提出;作为…的
about to
    即将，正要，刚要;欲
explanation
    n.解释;说明;辩解;（消除误会后）和解
tiny
    adj.极小的，微小的
    n.小孩子;[医]癣
related
    adj.有关系的;叙述的
    vt.叙述(relate过去式和过去分词)
break down
    失败;划分（以便分析）;损坏;衰弱下来
except that
    n.除了…之外，只可惜
asterisk
    n.星号，星状物
    vt.加星号于
parameter
    n.[数]参数;<物><数>参量;限制因素;决定因素
indenting
    n.成穴的
    v.切割…使呈锯齿状( indent的现在分词 );缩进排版
colon
    n.冒号;<解>结肠;科郎（哥斯达黎加货币单位
right away
    就;立刻，马上;当时
"""

# this one if like your scripts with argv
def print_two(*args):
    arg1, arg2, arg3 = args
    print(F"arg1: {arg1}\narg2: {arg2}\narg3: {arg3}\nargs: {args}")

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print(F"arg1: {arg1}\narg2: {arg2}")

# this just takes one argument
def print_one(arg1):
    print(F"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")


print_two("Zed", "Shaw", "ZhouGua")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()