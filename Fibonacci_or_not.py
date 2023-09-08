n=int(input())
a=0
b=1
x=0
for i in range(1,n+1):
    c=a+b
    if c<n:
        a=b
        b=c
    elif c==n:
        x=1
        break
    else:
        break
print(x==1)