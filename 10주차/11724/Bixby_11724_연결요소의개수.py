import sys
input=sys.stdin.readline
from collections import deque
def bfs(start):
    if visited[start]:return 0

    q=deque([start])
    visited[start]=True
    while q:
        v=q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i]=True
                q.append(i)
    return 1

n,m= map(int, input().split())
graph=[[]for _ in range(n+1)]
for _ in range(m):
    u,v= map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited=[False]*(n+1)
cnt=0

for i in range(1,n+1):
    cnt+=bfs(i)
print(cnt)