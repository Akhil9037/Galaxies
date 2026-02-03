from numpy import*
xlist=[]
ylist=[]
n=int(input("no of data points"))

for i in range(0,n):
    print("the x value",i+1)
    print("the y value",i+1)
    a=float(input())
    b=float(input())
    xlist.append(a)
    ylist.append(b)
xlist=array(xlist)
ylist=array(ylist)
print (xlist, ylist)
