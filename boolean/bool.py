#boolean represent the two values TRUE and FALSE 
#any string is true if its non empty empty string is always false
#any number is true except 0,or empty are false
#any list dictionary,list,tuple are true except empty
print(bool(""))
print(bool())
print(bool(None))
print(bool(False))
print(bool(0))
print(bool(()))
print(bool([]))
print(bool(""))
print(bool({}))

def myfuc():
    return True

if myfuc():
    print("yes")
else:
    print("no")

x =200
x = isinstance(x,int)
print(x)