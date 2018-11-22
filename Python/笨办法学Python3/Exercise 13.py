"""
Exercise 13: Parameters, Unpacking, Variables
    1.In this exercise we will cover one more input method you can use to pass variables to a scrip
    2.Write a script that has fewer arguments and one that has more
    3.Do it the way I do it and it’ll work.

parameters
    n.因素，特征;界限;（限定性的）因素( parameter的名词复数 );<物><数>参量;参项;决定因素;参数
unpacking
    n.取出货物，拆包[箱]
    v.拆包;从（包裹等）中取出（所装的东西），打开行李取出( unpack的现在分词 );解除…的负担;吐露（心事等）
feature
    n.特征，特点;容貌，面貌;（期刊的）特辑;故事片
    vt.使有特色;描写…的特征;以…为号召物
    vi.起主要作用;作重要角色
so that
    以便;结果，以致;俾
assigned
    n.[计][修]（已）赋值[分配];[计]指定的，赋值的
    adj.指定的，赋值的
    v.指定;指派;分配( assign的过去式和过去分词 );（作为说明或原因）提出
hold up
    举起;支撑;耽搁;持械抢劫
jargon
    n.行话;行业术语;黑话
stick
    vt.& vi.粘贴;张贴;插入;刺入
    vt.容忍;产生作用;（尤指迅速或随手）放置;阻延或推迟
    n.棍棒，棍枝;枝条;操纵杆;球棍
trick
    n.恶作剧;戏法，把戏;计谋，诀窍;骗局
    vt.哄骗，欺骗;打扮
    adj.弄虚作假的;有诀窍的;欺诈的
pay close attention to
    抓紧；密切关注
cause
    n.原因;事业;动机;理由
    vt.引起;导致;成为…的原因;使遭受
caused
    人为的
fewer
    pron.（动词用复数）较少数
    adj.较少的;很少;不多的( few的比较级 );（与复数名词和复数动词连用）有些;几个
overthink
    过度思考
replicate
    vt.复制，复写;重复，反复;折转;[生] 复制
    adj.复制的;折叠的;[植]折转的
    n.复制品;八音阶间隔的反覆音
stage
    n.阶段;舞台;戏剧;驿站
    vt.& vi.上演，演出;筹办，举行;适于上演;坐公共马车旅行
    vt.举行;展现;上演;筹划
    vi.适于上演，适合在舞台上演出;乘公交车（或驿车）旅行;[军事]中间集结，扎营
slap
    n.掌掴;侮辱;掌掴声
    vt.猛打;用力放置;尖刻批评、侮辱
    vi.拍击
    adv.直接地;猛然地
"""

#from sys import argv
# read the WYSS section for how to run this
#script, first, second, third = argv

#print("The script is called: ", script)
#print("Your first variable is: ", first)
#print("Your second variable is: ", second)
#print("Your third variable is: ", third)
#print(f"{argv}")

# Study Drills
#from sys import argv

#scriptName, firstArugument = argv

#print("This script name is", scriptName)
#print("%s World!!!" % firstArugument)
#print("argv =", argv)
#print("argv = %s" % argv)
#print(F"argv = {argv}")

from sys import argv

scriptName, first, second, third, forth = argv
print(F"argv = {argv}")
print(F"{first}, {second}")
print("What's your name? %s, Nice, %s." % (third, third))
print(F"The forth argv is {forth}")

print(F"The type of argv is {type(argv)}")
print(F"The type of first argument is {type(first)}")
