n=int(input())
for i in range(1,n+1):
    c=n
    for j in range(1,n+1):
        print(c,end=' ')
        c-=1
    print()