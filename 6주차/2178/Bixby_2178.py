def bfs(x=0,y=0):
    q = deque([(x,y)])
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if (0<=nx<n) and (0<=ny<m) and maze[nx][ny]==1:
                maze[nx][ny]=maze[x][y]+1
                q.append((nx,ny))
    return maze[n-1][m-1]

from collections import deque

n,m=map(int,input().split())
maze=[(list(map(int,input()))) for i in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]
print(bfs())