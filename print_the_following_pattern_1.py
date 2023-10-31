n=int(input())
for i in range(n,0,-1):
    c=1
    for j in range(1,i+1):
        print(c,end='')
        c+=1
    print()