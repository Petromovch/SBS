def dfs(graph,start,visited):
    visited.append(start)
    for i in graph[start]:
        if i not in visited:
            dfs(graph,i,visited)
n,m=map(int,input().split())
l=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    l[a-1].append(b-1)
    l[b-1].append(a-1)
visited=[]
dfs(l,0,visited)
if len(visited)==len(l):
    print("YES")
else:
    print("NO")


