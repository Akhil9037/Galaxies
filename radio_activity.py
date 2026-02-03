from numpy import*
from matplotlib.pyplot import*
from random import*


n=100
t=0.0
tmax=10.0
nlist=[]
tlist=[]
while n>0 and t<=tmax:
    for i in range(n):
        if random() <=1:
            n=n-1
    nlist.append(n)
    t=t+1
    tlist.append(t)
plot(tlist,nlist,"r")
ylist=(nlist[0]*exp(-1*array(tlist)))*.23
print(ylist)

plot(tlist,ylist)
show()
            
import numpy as np
import matplotlib.pyplot as plt
import random

n = 100
t = 0.0
tmax = 10.0
nlist = []
tlist = []

p = 0.1  # probability of removal per iteration

while n > 0 and t <= tmax:
    for i in range(n):
        if random.random() < p:   # FIXED condition
            n -= 1
    nlist.append(n)
    t += 1
    tlist.append(t)

plt.plot(tlist, nlist, "r", label="Simulation")

# Theoretical exponential decay
ylist = nlist[0] * np.exp(-p * np.array(tlist))
plt.plot(tlist, ylist, label="Exponential fit")
print(ylist[10])
print(ylist)

plt.legend()
plt.show()
