N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
graph[0] = [0,0]
visited = [False for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    graph[start].sort()
    graph[end].sort()

def DFS(graph, start, visited):
    visited[start] = True
    print(start, end=" ")

    for i in graph[start]:
        if not visited[i]:
            DFS(graph, i, visited)


def BFS(graph, start, visited):
    visited[start] = True
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")
        for i in graph[vertex]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


DFS(graph, V, visited)
visited = [False for _ in range(N+1)]
print()
BFS(graph, V, visited)