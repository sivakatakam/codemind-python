r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
a=0
for i in range(r):
    for j in range(c):
        if i==0 or j==0 or j==c-1 or i==r-1:
            a+=m[i][j]
print(a)