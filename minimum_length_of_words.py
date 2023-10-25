l=list(map(str,input().split()))
m=len(l[0])
for i in l:
    if m>len(i):
        m=len(i)
print(m)