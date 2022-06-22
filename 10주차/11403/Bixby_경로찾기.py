#입력
n=int(input())
reachable=[[0 for _ in range(n)] for i in range(n)]
graph=[list(map(int,input().split()))for _ in range(n)]
#플로이드워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            if not reachable[i][j]:
                reachable[i][j]=graph[i][j] or (graph[i][k] and graph[k][j])or (reachable[i][k] and reachable[k][j])
#출력
for column in reachable:
    print(*column)