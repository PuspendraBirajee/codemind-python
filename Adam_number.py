n=int(input())
sq=n*n
t=n
rev=0
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
revsq=rev*rev
revs=0
while revsq!=0:
    r1=revsq%10
    revs=revs*10+r1
    revsq=revsq//10
if revs==sq:
    print("True")
else:
    print("False")