def rev(s):
    return "".join(reversed(s))
l=list(map(str,input().split()))
for i in range(len(l)-1,-1,-1):
    print(rev(l[i]),end=' ')