t=int(input())
for i in range(t):
    s=input()
    x=0
    for i in range(len(s)):
        o=ord(s[i])
        if o>=48 and o<=57:
            x=x+1
    print(x==len(s))