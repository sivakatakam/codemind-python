n=int(input())
l=list(map(int,input().split()))
c=0
a=sum(l)//n
for i in l:
    if i<=a:
        c+=1
print(c)