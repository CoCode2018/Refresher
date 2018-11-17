"""
Exercise 5: More Variables and Printing
    1.do even more typing of variables and printing them out
    2.format string
    3. A string is how you make something that your program might give to a human.
    4.learn how to make strings that have variables embedded in them.
    5.You embed variables inside a string by using a special {} sequence and then put the variable you want inside the {} characters.
    6.You also must start the string with the letter f for "format"
    7."Hey, this string needs to be formatted. Put these variables in there."
    8.How can I round a floating point number?
        You can use the round() function like this: round(1.7333).

handy
    adj.方便的;手巧的;手边的，附近的;便于使用的
embedded
    adj.植入的，深入的，内含的
    v.把…嵌入，埋入( embed的过去式和过去分词 )
inside
    adj.里面的，内部的;内幕的;内侧的
    n.里面，内侧;内脏;内容，内幕;（道路或跑道拐弯处的）内侧
    adv.在内地，在内部地;在内侧地;在监狱里
    prep.在…以内;在内侧或内部;进入里面
usual
    adj.通常的，常有的，常见的;平常的，普通的;平时的，平日的;一向的，老是那一套的
as usual
    像往常一样;照旧;如故;仍然
even
    adv.甚至; 即使;更加;恰巧在…时候
    adj.公平的;平坦的; 偶数的;平均的
    vt.使平坦;使相等
    vi.变平;成为相等
even if
    哪怕;虽然;即使，纵然;即若
in event of
    万一， 如果 … 发生
inches
    n.英寸（相当于 2.54 厘米，一英尺有 12 英寸）( inch的名词复数 );少量;[复数]身材;（数量、距离、程度等）少许
lbs
    磅
teeth
    n.齿;牙( tooth的名词复数 );齿状部份;致力于（ 有难度的事）;tooth的复数形式;（组织、法律等）强大有效;不顾危险（或反对等）
so there
    （非正式）这是我最后的决定;再没有可说的;没有商量的余地;（事情）就是这样
convert
    vt.（使）转变;使皈依;兑换，换算;侵占
    vi.经过转变;被改变;[橄榄球] 触地得分后得附加分
    n.皈依者;改变宗教信仰者
centimeter
    n.厘米
kilogram
    n.公斤;千克
measurement
    n.量度;份量，尺寸;测量法;（量得的）尺寸
sense
    n.感觉，官能;意识，观念;理性;识别力
    vt.感到;理解，领会;检测出
make sense
    有意义;理解;讲得通;是明智的
weird
    adj.不可思议的;怪诞的，超自然的;奇怪的，奇异的;<古>命运的，宿命的
    n.命运，宿命;厄运;<古>命运女神
"""

my_name = 'Zed A. Shaw'
my_age = 35         # not a lie
my_height = 74      # inches
my_weight = 180     #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, tryto get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

# 空行
print()
print("==========Study Drills==========")
print()

print("===1===")
name = 'ZhouGua'
age = 23
height = 170 #cm
weight = 56  #kg
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height}cm tall.")
print(f"He's {weight}kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right.
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get{total}.")

print("===2===")
inches = float(input("Enter your tall in inches: "))
cm = round(2.57 * inches)
print(f"{inches} inches convert to centimeters are {cm}cm.")

pounds = float(input("Enter your heavy in pounds: "))
kg = round(0.45 * pounds)
print(f"{pounds} pounds convert to kilogram are {kg}kg.")




