import sys
input = sys.stdin.readline
inf = sys.maxsize

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

for k in range(n): # 경유지 노드
    for i in range(n): # 출발 노드
        for j in range(n): # 도착 노드
            if graph[i][k] and graph[k][j]:
                # [i][k] == 1 and [k][j] == 1이면 i -> j 로 갈 수 있다
                graph[i][j] = 1

for i in range(n):
    print(*graph[i])

# 플로이드 와샬 알고리즘
# i -> k 경로가 있고 k -> j 경로가 있으면 i -> j 경로가 존재한다