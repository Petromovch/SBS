from math import inf
n,m=map(int,input().split())
matrix=[[inf]*n for i in range(n)]
for i in range(m):
    a,b,c=map(int,input().split())
    matrix[a-1][b-1]=c
    matrix[b-1][a-1]=c






def deykstra(j):
    was=[]
    res=[inf for i in range(n)]
    res[j]=0
    for i in range(n):
        aim=inf
        aim_index=inf
        for r in range(n):
            if (res[r]<aim) and (not r in was):
                aim=res[r]
                aim_index=r
        was.append(aim_index)
        for i in range(n):
            res[i]=min(res[i],aim+matrix[aim_index][i])
    return res
print(sum(deykstra(0)))
    
