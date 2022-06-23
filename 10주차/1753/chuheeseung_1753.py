import sys
import heapq
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

v, e = map(int, input().split()) # 정점의 개수 : v, 간선의 개수 : e
k = int(input()) # 시작 정점의 번호 : k
INF = int(1e9)
graph = [[] * (v + 1) for _ in range(v + 1)] # 그래프 초기화
distance = [INF] * (v + 1) # 최단 거리 테이블 모두 무한으로 초기화

for _ in range(e): # 간선 정보 입력
    u, _v, w = map(int, input().split()) # u -> _v 간선 가중치 w
    graph[u].append((_v, w))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 시작 노드로 가기 위한 최단 경로는 0, 큐에 삽입
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q) # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기

        if distance[now] < dist: # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue

        for i in graph[now]: # 현재 노드와 연결된 다른 인접한 노드들을 확인
            cost = dist + i[1]

            if cost < distance[i[0]]: # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(k) # 다익스트라 알고리즘 수행

for i in range(1, v + 1): # 모든 노드로 가기 위한 최단 거리를 출력
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])