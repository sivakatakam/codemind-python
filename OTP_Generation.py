s=input()
c=''
for i in range(len(s)):
    if int(s[i])%2==1:
        c=c+str(int(s[i])*int(s[i]))
print(c)