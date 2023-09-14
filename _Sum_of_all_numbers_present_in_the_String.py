s=input()
c=0
for i in range(len(s)):
    o=ord(s[i])
    if o>=48 and o<=57:
        c=c+int(s[i])
print(c)