import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline


def dfs(graph, start, visited): # 돌면서 dfs 탐색
    visited[start] = True

    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n + 1)]
graph[0] = [0, 0]
visited = [False for _ in range(n + 1)]
count = 0

for _ in range(m): # graph 만들어놓기
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    graph[start].sort()
    graph[end].sort()

for i in range(1, len(visited)):
    if visited[i] == False: # 방문하지 않았으면 dfs 탐색
        count += 1 # 연결 요소의 개수 + 1
        dfs(graph, i, visited)

print(count)
