n=int(input())
for i in range(n):
    a=int(input())
    t=a
    rev=0
    while a!=0:
        r=a%10
        rev=rev*10+r
        a=a//10
    if t==rev:
        print("True")
    else:
        print("False")