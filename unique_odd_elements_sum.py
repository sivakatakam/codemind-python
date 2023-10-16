n=int(input())
s=set(map(int,input().split()))
l=list(s)
s=0
for i in l:
    if i%2==1:
        s+=i
print(s)