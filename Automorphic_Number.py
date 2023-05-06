n=int(input())
sq=n*n
t=n
c=0
while n!=0:
    r=n%10
    c+=1
    n=n//10
p=10**c
aut=sq%p
if aut==t:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")