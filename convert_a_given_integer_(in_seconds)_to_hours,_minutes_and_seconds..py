s=int(input())
h=s//3600
r=s%3600
m=r//60
se=r%60
print(f"H:M:S-{h}:{m}:{se}")