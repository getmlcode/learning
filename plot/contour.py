import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    return np.sin(x)**10+np.cos(y)**2+x*np.cos(2*x+10)

x=np.linspace(0,5,50)
y=np.linspace(0,5,50)

X,Y = np.meshgrid(x,y)

Z=f(X,Y)

plt.contour(X,Y,Z,colors='black')
plt.title('one')
plt.figure()
plt.title('two')
plt.contour(X,Y,Z,20,cmap='RdGy')

plt.figure()
plt.title('three')
plt.contourf(X,Y,Z,300,cmap='RdGy')
plt.colorbar()

plt.show(block=False)

input()