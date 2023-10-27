s=input()
v=input()
print(v in s)
for i in range(len(s)):
    if v==s[i]:
        print(i)
        break