r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
a=0
for i in range(r):
    for j in range(c):
        if i!=0 and j!=0 and j!=c-1 and i!=r-1:
            a+=m[i][j]
print(a)