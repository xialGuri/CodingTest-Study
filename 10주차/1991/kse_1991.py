n = int(input())
tree = {}
for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = (left, right)

result = [[] for _ in range(3)]
def dfs(node):
    if node != '.':
        result[0].append(node)
        dfs(tree[node][0])
        result[1].append(node)
        dfs(tree[node][1])
        result[2].append(node)

dfs('A')
print(''.join(result[0]))
print(''.join(result[1]))
print(''.join(result[2]))