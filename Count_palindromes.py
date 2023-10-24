def pal(n):
    x=int("".join(reversed(str(n))))
    if x==n:
        return 1
n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    if pal(i)==1:
        c+=1
print(c)