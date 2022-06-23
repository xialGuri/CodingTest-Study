import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

dp = [0] * (n + 1) # 인덱스 헷갈리지 않게 1~n 사용

for k in range(1, n + 1):
    dp[k] = dp[k-1] + arr[k-1] # 숫자의 누적합을 dp에 저장

for _ in range(m):
    i, j = map(int, input().split())
    print(dp[j] - dp[i-1]) # i~j 구간의 합 출력