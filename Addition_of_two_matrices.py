r=int(input())
a=[list(map(int,input().split())) for i in range(r)]
b=[list(map(int,input().split())) for i in range(r)]
for i in range(r):
    for j in range(r):
        print(a[i][j]+b[i][j],end=' ')
    print()