n=int(input())
k=n
for i in range(1,n+1):
    for j in range(k,0,-1):
        print(n+1-j,end=' ')
    k-=1
    print()