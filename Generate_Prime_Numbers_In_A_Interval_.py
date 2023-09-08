def isprime(n):
    x=0
    for i in range(2,n//2+1):
        if n%i==0:
            x=1
    if x==0:
        print(n)
a=int(input())
b=int(input())
for i in range(a,b+1):
    if i!=1:
        isprime(i)