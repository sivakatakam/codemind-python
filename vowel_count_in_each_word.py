def count(s):
    c=0
    v=['a', 'e', 'i', 'o', 'u']
    for i in s:
        if i in v:
            c+=1
    return c
l=list(map(str,input().split()))
for i in l:
    print(count(i),end=' ')