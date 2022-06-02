import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

def BFS(arr, visited, v):
    queue = deque()
    queue.append(v)
    color = arr[v[0]][v[1]]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for i in range(4):
            tempx = x + dx[i]
            tempy = y + dy[i]
            if not (0<=tempx<N and 0<=tempy<N):
                continue
            elif visited[tempx][tempy]:
                continue
            if color == arr[tempx][tempy]:
                queue.append((tempx, tempy))

arr1 = []

for _ in range(N):
    s1 = input()
    arr1.append(s1)


visited = [[False] * N for _ in range(N)]
cnt1, cnt2 = 0, 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(arr1, visited, (i, j))
            cnt1 += 1
visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            BFS(arr2, visited, (i, j))
            cnt2 += 1

print(cnt1, cnt2)