s=input()
v=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
x=[]
for i in s:
    if i in v:
        x.append(i)
        v.remove(i)
print(*x)