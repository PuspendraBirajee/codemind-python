import math
def prime(n):
    if(n<2):
        return 0
    for i in range(2,int(math.sqrt(n))+1):
        if(n%i==0):
            return 0
    return 1
a=int(input())
b=int(input())
c=0
for i in range(a,b+1):
    if(prime(i)):
        c+=1
print(c)
