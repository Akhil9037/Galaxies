from numpy import*
from numpy import*
xlist=[]
ylist=[]


n=int(input("enter the number of data points"))
for i in range(0,n):
     print(i)
     x=float(input())
     print(i)
     y=float(input())
     xlist.append(x)
     ylist.append(y)


h=xlist[1]-xlist[0]
I=ylist[0]+ylist[n-1]
for i in range(1,n-1,2):
    I=I+2*ylist[i]

for i in range(2,n-1,2):
     I=I+4*ylist[i]

I=I*h/3

print(I)

