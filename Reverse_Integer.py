def fun(n):
    rev=0
    while n:
        r=n%10
        n=n//10
        rev=rev*10+r
    return rev
n=int(input())
if n>0:
    x=fun(n)
else:
    n=n*-1
    x=fun(n)
    x=x*-1
print(x)