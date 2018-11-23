"""
Exercise 17: More Files
    1.This returns True if a ﬁle exists, based on its name in a string as an argument. It returns False if not. 
    2.from os.path import exists


handy
    adj.方便的;手巧的;手边的，附近的;便于使用的
second half
    后半部分
ton
    n.吨;大量，许多
blast
    n.爆炸;一阵（疾风等）;（吹奏乐器、哨子、汽车喇叭等突然发出的）响声;突如其来的强劲气流
    vt.击毁，摧毁;尖响;裁判高声吹哨;枯萎：使枯萎
    vi.爆炸;吼叫;枯萎：枯萎;攻击：严厉批评或猛烈攻击
crash
    v.碰撞;使发出巨响;暴跌;睡觉
    n.崩溃;碰撞;碰撞声;暴跌
    adj.应急的;速成的
annoying
    adj.恼人的;讨厌的
    v.骚扰(annoy的ing形式)
for a while
    adv.暂时;小
for a while now
    现在有一段时间了
totally
    adv.完全，整个地，全部地;百分之百;干净


"""
from sys import argv
from os.path import exists

script, from_file, to_file = argv
print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the outputfile exit? {exists(to_file)}")
print("Ready, hit RRTURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()


# Study Drills

# Try to make the script more friendly to use by removing features.

