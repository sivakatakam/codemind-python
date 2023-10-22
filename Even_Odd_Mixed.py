n=input()
e=0
o=0
for i in n:
    if int(i)%2==0:
        e+=1
    else:
        o+=1
if e==0:
    print("Odd")
elif o==0:
    print("Even")
else:
    print("Mixed")