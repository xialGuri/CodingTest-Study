def solution(n, k, cmd):
    linked_list = {i: [i - 1, i + 1] for i in range(1, n + 1)}
    k += 1
    result = ["O"] * (n)
    stack = []
    for s in cmd:
        count = 0
        if len(s) > 1:
            _, count = s.split()
            count = int(count)
        if s[0] == "D":
            for _ in range(count):
                k = linked_list[k][1]
        elif s[0] == "U":
            for _ in range(count):
                k = linked_list[k][0]
        elif s[0] == "C":
            prev, next = linked_list[k]
            stack.append((k, prev, next))
            result[k - 1] = "X"

            if prev == 0:
                k = linked_list[k][1]
                linked_list[next][0] = prev
            elif next == n + 1:
                k = linked_list[k][0]
                linked_list[prev][1] = next
            else:
                k = linked_list[k][1]
                linked_list[prev][1] = next
                linked_list[next][0] = prev
        elif s[0] == "Z":
            a, prev, next = stack.pop()
            result[a - 1] = "O"
            if prev == 0:
                linked_list[next][0] = a
            elif next == n + 1:
                linked_list[prev][1] = a
            else:
                linked_list[prev][1] = a
                linked_list[next][0] = a
    return "".join(result)

# 정확성 통과
# def solution(n, k, cmd):
#     arr = [i for i in range(n)]
#     stack = []
#     for s in cmd:
#         method = ""
#         count = 0
#         if len(s) > 1:
#             method, count = s.split()
#             count = int(count)
#         if s[0] == "D":
#             k = k+count
#         if s[0] == "U":
#             k = k-count
#         if s[0] == "C":
#             stack.append((k, arr[k]))
#             if k+1 == len(arr):
#                 arr.pop()
#                 k -= 1
#             else:
#                 arr = arr[:k] + arr[k+1:]
#         if s[0] == "Z":
#             a, b = stack.pop()
#             if a<=k:
#                 k+=1
#             arr = arr[:a] + [b]+ arr[a:]
#     cnt = 0
#     result = ""
#     for i in range(n):
#         if cnt >= len(arr):
#             result += "X"
#         elif arr[cnt] == i:
#             result += "O"
#             cnt+=1
#         else:
#             result += "X"
#     return result