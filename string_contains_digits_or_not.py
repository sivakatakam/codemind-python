t=int(input())
for i in range(t):
    s=input()
    c=0
    for i in range(len(s)):
        o=ord(s[i])
        if o>=48 and o<=57:
            c=1
            break
    if c==0:
        print("No")
    else:
        print("Yes")