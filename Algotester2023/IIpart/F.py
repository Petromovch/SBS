n=int(input())
a=list(map(int,input().split()))
dp1=[0]
for i in range(1,len(a)+1):
    dp1.append(dp1[-1]+a[-i])
dp2=[0]
for i in range(len(a)):
    dp2.append(dp2[-1]+a[i])
dp3=[0]
for i in range(1,len(dp2)):
    dp3.append(max(dp3[i-1],dp2[i]))
dp3.reverse()
dp4=[]
for i in range(len(dp3)):
    if dp1[i]<=dp3[i]:
        dp4.append(dp1[i])
print(max(dp4))

        
        
