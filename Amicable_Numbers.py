def pro(n):
    s=0
    for i in range(1,n//2+2):
        if n%i==0:
            s=s+i
    return s
n1=int(input())
n2=int(input())
if pro(n1)==n2 and pro(n2)==n1:
    print("Amicable")
else:
    print("Not Amicable")