s=input()
c=0
for i in s:
    if s.count(i)==1:
        c+=1
print(c==len(s))