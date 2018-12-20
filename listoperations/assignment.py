l=[1,2,3,4]
print('list = ', l)
nl=l
print('new list = ', nl)
nl[0]=33
print('changed new list = ', nl)
print('old list = ', l)

l=[1,2,3,4]
print('again changed old list = ', l)
nl=l[:]
nl[0]=33
print('again changed new list = ', nl)
print('again changed old list = ', l)
input()
