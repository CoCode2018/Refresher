"""
Exercise 16: Reading and Writing Files
    1.• close: Closes the ﬁle. Like File->Save... in your editor.
      • read: Reads the contents of the ﬁle. You can assign the result to a variable.
      • readline: Reads just one line of a text ﬁle.
      • truncate: Empties the ﬁle. Watch out if you care about the ﬁle.
      • write('stuff'): Writes “stuff” to the ﬁle.
      • seek(0): Moves the read/write location to the beginning of the ﬁle.
    2.One trick is to get bits of it running at a time.
    
actually
    adv.实际上;确实;竟;事实上
Neat
    整洁的
research
    n.调查;探索;研究，追究;探讨，探测
    vi.做研究;探究;（从市场调研中）得出所预测的结果
    vt.从事…的研究，为…而做研究
repetition
    n.重复，反复;背诵;复制品，副本;[乐]复唱，复奏，重奏
"""

from sys import argv

script, filename = argv

print(F"We're going to erase {filename}.")
print("If you don't want that, hit CTRT-C (^C).")
print("If you do want that, hit RETURN.")

input("?")
print("Opening the file....")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print("And finally, we close it.")
target.close()