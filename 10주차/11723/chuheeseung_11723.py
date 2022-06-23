import sys
input = sys.stdin.readline

m = int(input())
s = []

for i in range(m):
    a = input().split()

    if a[0] == "all": # s를 1~20으로 바꾼다
        s.clear()
        s = [i for i in range(1, 21)]
        continue
    elif a[0] == "empty": # s를 공집합으로 바꾼다
        s.clear()
        continue

    num = int(a[1])
    if a[0] == "add":
        if num not in s: # s가 이미 있는 경우에는 연산을 무시
            s.append(num)
    elif a[0] == "remove":
        if num in s: # s가 이미 있는 경우에는 연산을 무시
            s.remove(num)
    elif a[0] == "check":
        if num in s:
            print(1)
        else:
            print(0)
    elif a[0] == "toggle":
        if num in s:
            s.remove(num)
        else:
            s.append(num)