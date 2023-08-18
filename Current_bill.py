u=int(input())
if u<200:
    c=1.2
elif u<400:
    c=1.5
elif u<600:
    c=1.8
else:
    c=2
b=u*c
if b>400:
    t=b+(b*0.15)
else:
    t=100+b
print(f"{t:.2f}")