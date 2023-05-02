n=int(input())
s=0
t=n
for i in range(1,n,1):
    if n%i==0:
        s=s+i
if s==t:
    print("True")
else:
    print("False")
    