
var = 1000

def fun():
    global var;
    var = 1000+1000
    return var

def fun1():
    global var;
    var = 1000+1000+1000
    return var
print(fun())
print(fun1())
print(var)