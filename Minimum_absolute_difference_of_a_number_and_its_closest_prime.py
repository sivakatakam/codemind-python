def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    return c==2
n=int(input())
if prime(n):
    print(0)
else:
    i=n+1
    j=n-1
    while 1:
        if prime(i):
            d1=i-n
            break
        i=i+1
    while 1:
        if prime(j):
            d2=n-j
            break
        j=j-1
    print(min(d1,d2))