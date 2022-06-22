import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = list(map(int, input().split()))
sum_arr = []
sum = 0
for i in range(N):
    sum += arr[i]
    sum_arr.append(sum)

for _ in range(M):
    i, j = map(int, input().split())
    if i == 1:
        print(sum_arr[j-1])
    else:
        print(sum_arr[j-1]-sum_arr[i-2])
