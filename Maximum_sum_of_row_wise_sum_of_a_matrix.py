r,c=map(int,input().split())
m=[sum(list(map(int,input().split()))) for i in range(r)]
print(max(m))