import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
d=s*(s-a)*(s-b)*(s-c)
area=d**0.5
print("%.2f"%area)