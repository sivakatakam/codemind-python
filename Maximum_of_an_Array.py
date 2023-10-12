n=int(input())
l=list(map(int,input().split()))
m=l[0]
for i in range(1,n):
    if m<l[i]:
        m=l[i]
print(m)