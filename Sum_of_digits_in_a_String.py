s=input()
n=0
for i in range(len(s)):
    o=ord(s[i])
    if o>=48 and o<=57:
        n=n+int(s[i])
print(n)