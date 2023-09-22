def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    return c!=2
n=int(input())
c=0
for i in range(1,n+1):
    if n%i==0 and prime(i):
        c=c+1
print(c)