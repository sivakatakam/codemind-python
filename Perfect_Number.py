def per(a,b):
    if a==b:
        return "True"
    
    else:
        return "False"
n=int(input())
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
x=per(n,s)
print(x)