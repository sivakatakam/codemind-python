n=int(input())
l=list(map(int,input().split()))
e=0
o=0
for i in range(n):
    if l[i]%2==0:
        e+=1
    else:
        o+=1
print(f"{e} {o}")