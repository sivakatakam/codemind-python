s=input()
c=input()
a=0
for i in range(len(s)):
    if s[i]==c:
        a=a+1
if a==0:
    print(-1)
else:
    print(a)