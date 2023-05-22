n=int(input())
t=n
c=0
c1=0
c2=0
while n!=0:
    r=n%10
    c+=1
    n=n//10
while t!=0:
    re=t%10
    if re%2==0:
        c1+=1
    else:
        c2+=1
    t=t//10
if c1==c:
    print("Even")
elif c2==c:
    print("Odd")
else:
    print("Mixed")