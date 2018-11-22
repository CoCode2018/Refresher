"""
Exercise 15: Reading Files
    1.You may have to play with this exercise the most to understand what’s going on
    2.“Hard coding” means putting some bit of information that should come from the user as a string directly in our source code. 

erase
    vt.抹去;清除;擦掉
involve
    vt.包含;使参与，牵涉;围绕，缠绕;使专心于
plain
    n.平原;平地;[纺织业]平针;朴实无华的东西
    adj.平的;素的;清晰的;相貌平平的
    adv.清楚地，明白地;平易地;[用以加强语气]显然;完全地
    vi.发牢骚;诉苦
fancy
    vt.想像;设想;想要;猜想
    n.设想;想像力;爱好;怪想
    adj.（构思者）奇特的;昂贵的;（价格等）高价的;[美国俚语]真棒
    vi.想象，幻想
remainder
    n.剩余物;其他人员;差数;廉价出售的图书
    vt.廉价出售（书）;廉价出售
    adj.剩余的;留存下的
get rid of
    除掉，去掉;涤荡;革除;摈除
within
    adv.在内，在里面;在屋内;在心中，心里是
    prep.不超过，在…的范围内;在…能达到的地方;在…内，在…里面
    n.内部，里面
tape
    n.带子;卷尺;胶带，磁带
    vt.录音;用带子捆起来
    vt.& vi.录音
tape drive
    磁盘驱动器
restrict
    vt.限制，限定;约束，束缚
phrase
    n.成语;乐句;说法;<语>短语
    vt.叙述，措词
    vt.& vi.划分乐句，分乐节（尤指为奏乐或歌唱）

"""
# import sys module argv feature
from sys import argv

# unpacking argv to script and filename variables
script, filename = argv

#call open() function to open filename file and assignment to txt variable
txt = open(filename)

# print a string include filename variable
print(F"Here's your file {filename}:")

# call read() function to read txt file conten and print
print(txt.read())
txt.close()
# prompt and get a file name
print("Type the filename again: ")
file_again = input(">")

# open the input name file
txt_again = open(file_again)

# read and print the file
print(txt_again.read())
txt_again.close()

