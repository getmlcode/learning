from functools import reduce
def inc(x): return x+23
l=[1,2,3,4,5]

print(list(map(inc,l)))

print(list(map(lambda x:x**2,l)))

print(set(map(lambda x:x**2,l)))

print(list(filter(lambda x:x==x**2-20,[1,2,5,6,7])))

print(reduce(lambda x,y:x+y, [[1,2],[3,4],[1,3,4]]))

