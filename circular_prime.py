def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    return c==2
n=int(input())
s=int("".join(reversed(str(n))))
if prime(n) and prime(s):
    print("circular prime")
elif prime(n) or prime(s):
    print("prime but not a circular prime")
else:
    print("not prime")