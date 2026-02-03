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
num=(n*sum(xlist*ylist)-sum(xlist)*sum(ylist))
den=n*sum(xlist*xlist)-(sum(xlist))**2
m=num/den
c=(sum(ylist)-m*sum(xlist))/n
print("y=",m,"x+",c)
    
