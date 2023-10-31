n=int(input())
c=n
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==i or j==c:
            print('x',end='')
        else:
            print(0,end='')
    c=c-1
    print()