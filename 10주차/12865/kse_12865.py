# from collections import deque
#
# N, K = map(int, input().split())
# things = deque()
#
# for _ in range(N):
#     w, v = map(int, input().split())
#     things.append([w, v])
#
# dp = [[0 for _ in range(K+1)] for _ in range(N)]
#
# for i in range(N):
#     w, v = things.popleft()
#     for j in range(K+1):
#         if i == 0:
#             if j >= w:
#                 dp[i][j] = v
#         else:
#             if j < w:
#                 dp[i][j] = dp[i-1][j]
#             else:
#                 dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j])
#
#
# print(dp[-1][-1])

N, K = map(int, input().split())

WV = [list(map(int, input().split())) for _ in range(N)]

WV.sort()
dp = [0] * (K+1)
for w, v in WV:
    for i in range(K, -1, -1):
        if i - w < 0:
            break
        dp[i] = max(dp[i-w] + v, dp[i])

print(dp[K])