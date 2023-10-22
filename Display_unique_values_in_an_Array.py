n=int(input())
l=list(map(int,input().split()))
x=[]
for i in l:
    if l.count(i)==1:
        x.append(i)
if len(x)==0:
    print(-1)
else:
    print(*x)