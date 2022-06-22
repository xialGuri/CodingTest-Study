import sys

input = sys.stdin.readline

s = set()

M = int(input())

for _ in range(M):
    data = input().strip()
    if data == "all":
        s = set([i for i in range(1,21)])
        continue
    elif data == "empty":
        s = set()
        continue
    fun, num = data.split()
    num = int(num)
    if fun == "add":
        s.add(num)
    elif fun == "remove":
        if num in s:
            s.remove(num)
    elif fun == "toggle":
        if num in s:
            s.remove(num)
        else:
            s.add(num)
    elif fun == "check":
        if num in s:
            print(1)
        else:
            print(0)