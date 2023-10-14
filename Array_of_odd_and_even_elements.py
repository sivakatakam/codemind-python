n=int(input())
l=list(map(int,input().split()))
le=[]
lo=[]
for i in l:
    if i%2==0:
        le.append(i)
    else:
        lo.append(i)
s=lo+le
print(*s)