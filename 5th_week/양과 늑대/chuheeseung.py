def solution(info, edges):
    def nextNodes(v):
        temp = list()

        for e in edges:
            i, j = e # i는 부모노드, j는 자식노드
            if v == i: # 부모노드의 번호를 비교
                temp.append(j)

        return temp

    def dfs(sheep, wolf, current, path): # 지금 노드를 확인, 양과 늑대 판별
        if info[current]:
            wolf += 1
        else:
            sheep += 1

        if sheep <= wolf: # 늑대가 양을 다 잡아먹어서 바로 0 리턴
            return 0

        maxSheep = sheep # 아니면 임시 변수에 값 갱신

        for p in path: # 탐색 시작
            for n in nextNodes(p):
                if n not in path:
                    path.append(n)
                    maxSheep = max(maxSheep, dfs(sheep, wolf, n, path)) # 최대 양 판별
                    path.pop()

        return maxSheep

    answer = dfs(0, 0, 0, [0])

    return answer



print(solution([0,0,1,1,1,0,1,0,1,0,1,1],
               [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))

print(solution([0,1,0,1,1,0,1,0,0,1,0],
               [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))