n,m=map(int,input().split())
key=[]
new=[]
for i in range(n):
    a=list(map(int,input().split()))
    new.extend(a)
new.sort()
for i in range(1,len(new)):
    if new[i]==new[i-1]:
        key.append(new[i])
print(len(key))
print(*key)
        
    
    
        
