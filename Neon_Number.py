n=int(input())
s=n**2
x=0
while s!=0:
    r=s%10
    s=s//10
    x=x+r
if x==n:
    print("Neon Number")
else:
    print("Not Neon Number")