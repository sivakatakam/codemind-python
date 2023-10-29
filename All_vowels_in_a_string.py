s=input()
c=['A', 'E', 'I', 'O', 'U']
v=['a', 'e', 'i', 'o', 'u']
for i in s:
    if i in c:
        c.remove(i)
    elif i in v:
        v.remove(i)
print(len(c)==0 or len(v)==0)