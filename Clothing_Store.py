n=int(input())
l=list(map(int,input().split()))
s=set(l)
p=0
for i in s:
    c=l.count(i)
    p=p+c//2
print(p)