"""
Exercise 12: Prompting People
    1.

prompting
    n.暗示，提示;刺激，鼓励;煽动，驱使
    v.推动，提示，鼓舞(prompt的现在分词)
parenthesis
    n.圆括号;插入语;插入成分;间歇
alright
    adv.好的;正确;令人满意
    adj.没问题的
but then
    但另一方面是
"""

age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh?")

print(F"SO, you're {age} old, {height} tall and {weight} heavy.")

# Study Drills
# 1. run pydoc / python -m pydoc
#   pydoc - the Python documentation tool
# 2. quit pydoc
#    Get out of pydoc by typing q to quit.
# 3.pydoc command does

# 4.


age = input("How old are you?")
height = input(F"You're {age}? Nice. How tall are you?")
weight = input(F"You're {age}? Nice. You're {height}? Good. How much do you weight?")
print(F"So, you're {age} old, {height} tall and {weight} heavy.")

print("How old are you? ",input("\t>>>"))