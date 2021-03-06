#!/usr/bin/env python

from mpl_toolkits.mplot3d import Axes3D
import random
import numpy as np
import matplotlib.pyplot as plt
import sys,math

'''
1. Starting point is x=0,
2. Unit steps 
3. any direction ()
2. Amazingly, it has been proven that on a two-dimensional lattice, 
a random walk has unity probability of reaching any point
(including the starting point) as the number of steps approaches infinity.
'''
X = [0]
Y = [0]
point=[]
#x_initial = random.uniform(-1,1)
#y_initial = math.sqrt(1-x_initial**2)
def rand_walks(x_loc,y_loc):
    x=random.uniform(-1,1)
    y_pos = math.sqrt(1-x**2)
    y_neg = -y_pos
    y= random.choice([y_pos,y_neg])
    print '( ',x,',',y,')'
    print x**2+y**2
    return [x+x_loc,y+y_loc]


while len(X)<=1000:
	points = rand_walks(X[-1],Y[-1])
        X.append(points[0])
        Y.append(points[1])
        print points
        


'''
ax = fig.add_subplot(111, projection='3d')
hist = np.histogram2d(X,Y, bins=40)
#plt.colorbar()
ax.bar3d()
plt.show()
exit()
plt.hist(X,bins=100)
plt.hist(Y,bins=100)
plt.subplots_adjust(left=0.15)
'''
#3D-plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
hist, xedges, yedges = np.histogram2d(X, Y, bins=20)
elements = (len(xedges) - 1) * (len(yedges) - 1)
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25)
xpos = xpos.flatten()
ypos = ypos.flatten()
zpos = np.zeros(elements)
dx = 0.5 * np.ones_like(zpos)
dy = dx.copy()
dz = hist.flatten()
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color='b', zsort='average')

plt.show()





































