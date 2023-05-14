n=int(input())
sq=n*n
rev=0
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
rsq=rev*rev
rev1=0
while rsq!=0:
    r1=rsq%10
    rev1=rev1*10+r1
    rsq=rsq//10
if rev1==sq:
    print("True")
else:
    print("False")