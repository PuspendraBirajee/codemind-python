n=int(input())
c=0;
for i in range(2,n):
    if(n%i==0):
        print(i,end=" ")
        c=1
        
if(c==0):
    print("-1")
    
