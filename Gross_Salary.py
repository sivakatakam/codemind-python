b=int(input())
if b<=10000 :
    d=(b/100)*80
    h=(b/100)*20
elif b<=20000 :
    d=(b/100)*90
    h=(b/100)*25
else :
    d=(b/100)*95
    h=(b/100)*30
g=b+d+h
print("%.2f"%g)