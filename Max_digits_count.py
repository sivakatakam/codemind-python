n=int(input())
l=list(map(str,input().split()))
m=len(l[0])
c=0
for i in l:
    if len(i)>m:
        m=len(i)
for i in l:
    if len(i)==m:
        c+=1
print(c)