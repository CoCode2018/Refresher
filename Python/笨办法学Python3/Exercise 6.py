# -*- encoding: utf-8 -*-
"""
Exercise 6: Strings and Text
    1.We'll cover that more later.
    2.Programmers love saving time at your expense by using annoyingly short and cryptic variable names


while
    conj.而;虽然;在…期间;与…同时
    n.（一段）时间
    vt.消磨，打发（时间）;（愉快而懒散地）度过（时间）（常与 away 连用）
a bunch of
    一群;一束;一堆;班
explanation
    n.解释;说明;辩解;（消除误会后）和解
export
    vt.& vi.出口，输出
    vt.传播，输出（思想或活动）
    n.输出，出口;输出[出口]物
abbreviated
    adj.简短的，仅可蔽体的，小型的
    v.缩略;使简短( abbreviate的过去式和过去分词 );缩简;使用缩写词
expense 
    n.费用;花费的钱;消耗;花钱的东西
    vt.向…收取费用;把…作为开支勾销
annoyingly 
    adv.恼人地，烦人地
cryptic 
    adj.神秘的;隐藏的;有隐含意义的;使用密码的
hilarious
    adj.欢闹的;令人捧腹的;非常滑稽的;喜不自禁的
evaluation 
    n.估价;<数>赋值;估计价值;[医学]诊断
"""

types_of_people = 10
x = "There are {type_of_people} types of people."

binary = "binary"
do_not = "don't"
y = "Those who konw {binary} and those who {do_not}."

print(x)
print(y)

#print(f"I said: {x}")
#print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w +e)