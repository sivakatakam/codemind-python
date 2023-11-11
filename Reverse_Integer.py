n=int(input())
s=0
if n>0:
    x=1
else:
    n=n*-1
    x=-1
while n>0:
    r=n%10
    n=n//10
    s=s*10+r
print(s*x)