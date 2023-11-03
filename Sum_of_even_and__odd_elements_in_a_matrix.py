r,c=map(int,input().split())
m=[list(map(int,input().split())) for i in range(r)]
e=0
o=0
for i in range(r):
    for j in range(c):
        if m[i][j]%2==0:
            e+=m[i][j]
        else:
            o+=m[i][j]
print(e,o)