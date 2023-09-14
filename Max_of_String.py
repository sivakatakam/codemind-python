s=input()
m=0
for i in range(len(s)):
    o=ord(s[i])
    if m<o:
        m=o
print(chr(m))