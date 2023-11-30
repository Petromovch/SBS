n=int(input())
for i in range(n):
    a=list(input())
word=list(input())
dp=[[0]*n for i in range(n)]
if a[0]==word[0]:
    dp[0][0]=1
else:
    print(0)
for i in range(1,n):
    if a[0][i]==word[0][i]:
        dp[0][j]=dp[0][j-1]
    else:
        continue
for i in range(1,n):
    for j in range(1,n):
        if a[i][j]==word[i]:
            dp[i][j]=dp[i-1][j-1]+dp[i-1][j]+dp[i-1][j+1]
        else:
            continue
for i in dp:
    print(i)
print(dp[-1][-1])
            
