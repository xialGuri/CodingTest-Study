import sys

input = sys.stdin.readline

N = int(input())

arr = []
for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)

graph = [[] for i in range(N)]
def dfs(graph, v, visited):

    for i in graph[v]:
        if not visited[i]:
            visited[i] = 1
            dfs(graph, i, visited)

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            graph[i].append(j)

result =[]
for i in range(N):
    visited = [0]*N
    dfs(graph, i, visited)
    result.append(visited)
for i in result:
    for j in i:
        print(j, end=" ")
    print()