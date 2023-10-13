n=int(input())
l=list(map(int,input().split()))
a=0
b=0
c=0
for i in range(1,n-1):
    if l[i-1]%2==0:
        b=1
    else:
        b=0
    if l[i+1]%2==0:
        a=1
    else:
        a=0
    if a!=b:
        c+=1
print(c)