x=int(input()) 
n=list(map(int,input().split()))
s=0
for i in range(x):
    if i%2==1:
        s=s+n[i]
print(s)