n = int(input())

m = int(input())
if m != 0:
    arr = list(map(int, input().split()))
else:
    arr = []
num = 100

ans = abs(n - 100)
for i in range(1000001):
    numArr = list(str(i))
    flag = False
    # 숫자를 누를 수 있는 지 검사
    for k in numArr:
        if int(k) in arr:
            flag = True
            break

    if flag:
        continue
    # 해당 숫자를 누를 수 있다면 n까지 가는 방법 + 숫자를 누른횟수를 구해서 비교한다.
    else:
        ans = min(ans, abs(n - i) + len(str(i)))

print(ans)