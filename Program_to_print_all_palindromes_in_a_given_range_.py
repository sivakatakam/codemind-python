def pal(n):
    s=str(n)
    x="".join(reversed(s))
    if x==s:
        print(x,end=' ')
a=int(input())
b=int(input())
for i in range(a,b+1):
    pal(i)