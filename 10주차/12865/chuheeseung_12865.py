import sys
input = sys.stdin.readline

def bagpack(n, k, items): # 가방 싸는 함수
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1): # 가방에 담을 수 있는 물건의 개수를 하나씩 늘려나간다
        weight, value = map(int, items[i-1])

        for j in range(1, k + 1): # 가방에 담을 수 있는 최대 무게를 1씩 차례대로 늘려나간다
            if weight <= j: # 현재 물건이 가방에 담을 수 있는 무게보다 작으면
                # 현재 물건을 넣지 않았을 때, 현재 물건을 넣었을 때 가치를 비교
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)
            else:
                dp[i][j] = dp[i-1][j] # 이전 물건까지 담았을 때 가방에 담을 수 있는 최고 가치를 저장

    print(dp[n][k]) # 가방에 담을 수 있는 최대 무게에서 모든 물건을 고려했을 때의 최댓값 출력

n, k = map(int, input().split()) # n : 물건 개수, k : 가방에 담을 수 있는 최대 무게
items = [list(map(int, input().split())) for _ in range(n)] # 각 물건의 무게와 가치
bagpack(n, k, items) # 주어진 조건으로 가방 싸기