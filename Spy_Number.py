n=int(input())
s=0
m=1
while n>0:
    r=n%10
    n=n//10
    s=s+r
    m=m*r
if s==m:
    print("Spy Number")
else:
    print("Not Spy Number")