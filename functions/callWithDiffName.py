def f():
    print('this was called using newname')

def g():
    print("this was called using name f")

newname = f
newname()

f=g
f()

input('press enter to exit')

