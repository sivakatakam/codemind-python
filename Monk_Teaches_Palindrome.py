t=int(input())
for i in range(t):
    s=input()
    if s=="".join(reversed(s)):
        if len(s)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")