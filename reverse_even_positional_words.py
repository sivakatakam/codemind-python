def rev(s):
    return "".join(reversed(s))
l=list(map(str,input().split()))
for i in range(len(l)):
    if i%2==0:
        print(rev(l[i]),end=' ')
    else:
        print(l[i],end=' ')