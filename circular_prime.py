def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    return c==2
n=int(input())
s=str(n)
r=int(s[::-1])
if prime(n) and prime(r):
    print("circular prime")
elif prime(n):
    print("prime but not a circular prime")
else:
    print("not prime")