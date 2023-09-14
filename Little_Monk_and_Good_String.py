s=input()
x=['a','e','i','o','u']
c=0
m=0
for i in range(len(s)):
    if s[i] in x:
        c=c+1
    else:
        c=0
    if m<c:
        m=c
print(m)