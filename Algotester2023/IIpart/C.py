l=int(input())
k=0
for n in range(1,l+1):
    x=n*(n+1)+n*(n+1)//2
    k+=x
print(k)
