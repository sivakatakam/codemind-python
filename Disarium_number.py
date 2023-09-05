n=int(input())
x=n
l=len(str(n))
s=0
while n:
    r=n%10
    n=n//10
    s=s+r**l
    l=l-1
print(s==x)