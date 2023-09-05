n=int(input())
s=n**2
r=int(''.join(reversed(str(n))))
sr=int(''.join(reversed(str(r**2))))
print(sr==s)