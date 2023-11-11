t=int(input())
for i in range(t):
    n=input()
    s="".join(reversed(n))
    print(s==n)