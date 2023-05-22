a=int(input())
arr=list(map(int,input().split()))
if(len(set(arr))==1):
    print(0)
else:
    c=0
    mc=0
    for i in range(a):
        c=0
        for j in range(i,a):
            if(arr[i]==arr[j]):
                c+=1
                if(mc<c):
                    mc=c
    print(mc)
