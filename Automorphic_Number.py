n=int(input())
p=n**2
d=p%(10**(len(str(n))))
if d==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")