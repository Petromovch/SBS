n,a0,a1=map(int,input().split())
def getsign(a):
    if a==0:
        return "0"
    if a>0:
        return "+"
    if a<0:
        return "-"
def time():
    if n==0:
        return getsign(a0)
    if n==1:
        return getsign(a1)
    if getsign(a0)==getsign(a1):
        return getsign(a0)
    if a0==0:
        return getsign(a1)
    if a1==0:
        return getsign(a0)
    return False
t=time()
while t==False:
    a0,a1,n=a1,a0+a1,n-1
    t=time()
print(t)
    
    
