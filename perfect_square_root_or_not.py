n=int(input())
x=0
for i in range((n//2)+1):
    if i*i==n:
        x=1
print(x==1)