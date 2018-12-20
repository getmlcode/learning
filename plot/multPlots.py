import matplotlib.pyplot as plt
import numpy as np

ax1=plt.axes()
plt.axes([.5,.5,.2,.2])
plt.axes([.3,.3,.19,.3])

x=np.linspace(0,20)

fig1 = plt.figure()
ax1=fig1.add_axes([.1,.5,.8,.4],xticklabels=[],ylim=[-1.2,1.2])
ax2=fig1.add_axes([.1,.1,.8,.4],ylim=[-1.2,1.2])
ax1.plot(np.sin(x))
ax2.plot(np.cos(x))

fig2 = plt.figure()
ax1=fig2.add_axes([.1,.5,.8,.4],xticklabels=[],ylim=[-1.2,1.2])
ax2=fig2.add_axes([.1,.1,.8,.4],ylim=[-1.2,1.2])
ax1.plot(np.cos(x))
ax2.plot(np.sin(x))

fig3=plt.figure()
for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2, 3, i)),fontsize=12, ha='center')

fig4=plt.figure()
fig4.subplots_adjust(hspace=.4,wspace=.4)
for i in range(1, 7):
    plt.subplot(2, 3, i)
    plt.text(0.5, 0.5, str((2, 3, i)),fontsize=12, ha='center')

fig5, ax = plt.subplots(3, 4, sharex='col', sharey='row')
for i in range(3):
    for j in range(4):
        ax[i, j].text(0.5, 0.5, str((i+1, j+1)),fontsize=12, ha='center')
        ax[i, j].set_title('graph'+str(4*i+j+1),fontsize=12)

plt.subplots(4, 2, sharex='col', sharey='row')
plt.show(block=False)
input('Enter To Txit')
