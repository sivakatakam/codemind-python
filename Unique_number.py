x=input()
l=list(x)
s=set(x)
if len(l)==len(s):
    print("Unique Number")
else:
    print("Not Unique Number")