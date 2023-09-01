n=int(input())
x=0
while n!=0:
    r=n%10
    n=n//10
    if x<r:
        x=r
print(x)