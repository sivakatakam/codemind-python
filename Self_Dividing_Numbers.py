def fun(n):
    x=n
    c=0
    d=0
    while n!=0:
        r=n%10
        n=n//10
        if r!=0:
            if x%r==0:
                c=c+1
        d=d+1
    if c==d:
        print(x,end=' ')
a=int(input())
b=int(input())
for i in range(a,b+1):
    fun(i)