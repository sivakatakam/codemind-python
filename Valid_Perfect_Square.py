t=int(input())
for i in range(t):
    n=int(input())
    c=0
    for i in range(1,n+1):
        if n==i*i:
            c=1
            break
    print(c==1)