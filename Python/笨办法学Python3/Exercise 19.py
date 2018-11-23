"""
Exercise 19: Functions and Variables
    1.

amount of information
    信息量
mind-blowing
    adj.引起幻觉的，使兴奋的
eventually
    adv.终究;终于，最后;竟;总归
reinforce
    vt.加固;强化;增援
    vi.求援;得到增援;给予更多的支持
    n.加强;加固物;加固材料
right now
    此时;立即;此刻，目前

"""

def cheese_and_crackers(cheese_cont, boxes_of_crackers):
    print(f"You have {cheese_cont} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly: ")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50

