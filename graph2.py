def dfs(graph,start,visited):
    count_edges=0
    visited[start]=1
    for i in graph[start]:
        count_edges+=1
        if visited[i]==0:
            count_edges=count_edges+dfs(graph,i,visited)
    return count_edges
n,m=map(int,input().split())
graph=[[] for i in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
components=0
visited=[0 for i in range(n)]
counts=[]
for i in range(n):
    if visited[i]==0:
        counts.append(dfs(graph,i,visited)//2)
        components+=1
print(components-1)
