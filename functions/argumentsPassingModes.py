def argumentPass(a,b,c):
    print(a,b,c)

def positionalNameMatching(d,a,b,c):
    print(a,b,c,d)


a=1
b=2
c=3
print("original order : 1-2-3")
print("positional ")
argumentPass(1,2,3)

print("original order : 3-2-1" )
print("match by name")
argumentPass(c=3,b=2,a=1)

print("original order : 5-3-2-1" )
print("positional and name matching")
positionalNameMatching(5,c=3,b=2,a=1)
