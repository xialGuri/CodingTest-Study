def bfs(x=0,y=0):
    q = deque([(x,y)])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if (-1<nx<n) and (-1<ny<m) and graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                q.append((nx,ny))
    return graph[n-1][m-1]

from collections import deque

n,m=map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx= [-1, 1, 0, 0]
dy= [0, 0, -1, 1]
print(bfs())