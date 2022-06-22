import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[]for i in range(N)]
for i in range(M):
    u, v = map(int,input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

def dfs(graph, v, visited):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

result = 0
visited = [False] * (N)
for i in range(N):
    if not visited[i]:
        dfs(graph, i, visited)
        result +=1

print(result)