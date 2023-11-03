r=int(input())
c=int(input())
m=[list(map(int,input().split()))[:c:] for x in range(r)]
a=0
for i in m:
    for j in i:
        a+=j
print(a)