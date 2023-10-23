def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c=c+1
    if c==2:
        return 1
n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=0
for i in l:
    if i>=k:
        if prime(i)==1:
            s=s+1
print(s)