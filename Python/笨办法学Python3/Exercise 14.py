# -*- encoding: UTF-8 -*-
"""
Exercise 14: Prompting adn Passing

specific
    adj.具体的;明确的;特种的;[免疫学]特效的
    n.特效药;特性;细节;显著的性质，特性
slightly
    adv.轻微地，轻轻地;细长地，苗条地;〈罕〉轻蔑地;粗
spot
    n.地点，场所;斑点，污点;[股票]现货;职位，职务
    v.弄上污渍，弄上斑点;污辱，玷污;认出，发现;散步
    adj.现场的;现货的;插播的
    abbr.satellite positioning and tracking 卫星定位和跟踪
entirely
    adv.完全地;完整地;全部地;彻底地
totally
    adv.完全，整个地，全部地;百分之百;干净
"""

from sys import argv

script, user_name = argv
prompt = '>'

print(F"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")

print(F"Dou you like me {user_name}?")
likes = input(prompt)

print(F"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(F"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
"""
)

# Study Drills
