a=list(map(int,input().split()))
c=[0]
pos=0
for i in range(1,len(a)):
    if i<=pos+a[pos]:
        c.append(c[pos]+1)
    else:
        while i>pos+a[pos]:
            pos+=1
        c.append(c[pos]+1)
print(c)
print(c[-1])
