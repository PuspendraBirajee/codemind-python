import math
n,x=map(int,input().split())
r=n%(10**x)
t=n
c=0
while n!=0:
    rem=n%10
    c+=1
    n=n//10
c1=c-x
q=t//(10**c1)
d=abs(r-q)
print(d)