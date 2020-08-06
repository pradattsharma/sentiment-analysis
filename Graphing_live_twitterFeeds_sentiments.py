import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

style.use('ggplot')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

#ax1 = fig.add_subplot(2, 2, 2)

def animate(i):
    pull_data = open('twitter-output.txt', 'r').read()
    lines = pull_data.split('\n')
    
    xarr = []
    yarr = []
    
    x = 0
    y = 0
    
    for l in lines:
        x += 1
        if 'pos' in l:
            y += 1
        elif 'neg' in l:
            y -= 0.1  #biased towards negative sentiments
            
        xarr.append(x)
        yarr.append(y)
        
    ax1.clear()
    ax1.plot(xarr, yarr)
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
    