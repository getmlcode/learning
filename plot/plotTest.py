from matplotlib import pyplot as plt
from matplotlib import style

#Graph
style.use('ggplot')
x=[5,8,10]
y=[12,16,6]
x2=[6,9,11]
y2=[6,9,11]

graph = plt.figure(1)
plt.plot(x,y)

plt.title("Info")

plt.plot(x,y,'g',label='line-1',linewidth=2)
plt.plot(x2,y2,'k',label='line-2',linewidth=2)

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')

plt.legend()
plt.grid(True,color='k')

graph.show()


#Bar Graph
bar = plt.figure(2)
plt.bar([1,3,4,7,9],[5,2,7,8,2],label='Ex-1')
plt.bar([2,4,6,8,10],[8,6,2,5,6],label='Ex-2',color='g')

plt.legend()
plt.xlabel('bar number')
plt.ylabel('bar heighnt')

plt.title('Bar graph')
bar.show()

#Scatter Plot
scatter = plt.figure(3)
x3=[1,2,3,4,5,6,7,8]
y3=[3,5,7,8,9,10,1,13]

plt.scatter(x,y,label='skitscat',color='b',marker="o")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
scatter.show()

#Pie Chart

slices=[7,23,4,8]
acts = ['sleep','eat','work','play']
cols=['c','m','r','g']
pchrt=plt.figure(4)
plt.pie(slices,labels=acts,colors=cols,shadow=True,startangle=0,
        explode=(0.1,0.4,0,0),autopct='%1.1f%%')
plt.title('PieChart')
pchrt.show()

input()
