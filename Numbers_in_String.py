s=input()
sum=0
for i in s:
    if i in "0123456789":
        l=i
        k=int(l)
        sum=sum+k
print(sum)