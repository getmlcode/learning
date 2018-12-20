l=[1,2,3,4,5]
res=[[2**x,x**2] for x in l]
print(res)

res=[[2**x,x**2] for x in l if x%2==0]
print(res)
