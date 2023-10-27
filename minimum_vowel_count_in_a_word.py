def count(s):
    v=['a', 'e', 'i', 'o', 'u']
    c=0
    for i in s:
        if i in v:
            c+=1
    return c
l=list(map(str,input().split()))
x=[]
for i in l:
    x.append(count(i))
print(min(x))