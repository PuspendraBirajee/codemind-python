n=int(input())
while n>9:
    r=n%10
    n=n//10
    n=n+r
print(n)