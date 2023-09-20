def pal(n):
    r=int("".join(reversed(str(n))))
    return r==n
n=int(input())
i=n+1
j=n-1
while 1:
    if pal(i):
        d1=i
        break
    i=i+1
while 1:
    if pal(j):
        d2=j
        break
    j=j-1
if abs(d1-n)==abs(d2-n):
    print(d2, d1)
elif abs(d1-n)<abs(d2-n):
    print(d1)
else:
    print(d2)