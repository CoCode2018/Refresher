# thismod.py

var = 99
def local():
    var = 0
    print(f"local_var = [{var}]", end = '\n')


def glob1():
    global var
    print(f"glob1_var = [{var}]", end = '\n')
    var += 1
    print(f"glob1_var = [{var}]", end = '\n')

def glob2():
    var = 0
    print(f"glob2_var = [{var}]", end = '\n')
    import thismod
    print(f"glob2_var = [{var}]", end = '\n')
    print(f"glob2_var = [{thismod.var}]", end = '\n')
    thismod.var += 1
    print(f"glob2_var = [{var}]", end = '\n')
    print(f"glob2_var = [{thismod.var}]", end = '\n')

def glob3():
    var = 0
    print(f"glob3_var = [{var}]", end = '\n')
    import sys
    glob = sys.modules['thismod']
    print(f"glob3_var = [{var}]", end = '\n')
    print(f"glob3_var = [{glob.var}]", end = '\n')
    glob.var += 1
    print(f"glob3_var = [{var}]", end = '\n')
    print(f"glob3_var = [{glob.var}]", end = '\n')


def test():
    print(var)
    local()
    glob1()
    glob2()
    glob3()
    print(var)



