n=int(input())
s=list(input())
dp=[0 for i in range(n)]
for i in range(n):
    if s[i]=="*":
        dp[i]=s[i]
if dp[0]!="*" and dp[1]=="*":
    dp[0]=1
if dp[-1]!="*" and dp[-2]=="*":
    dp[-1]=1
for i in range(1,n-1):
    if dp[i]!="*":
        if dp[i+1]=="*":
            dp[i]+=1
        if dp[i-1]=="*":
            dp[i]+=1
for i in range(n):
    print(dp[i],end="")
