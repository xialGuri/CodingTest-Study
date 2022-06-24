m = int(input())
s= [0] * 21
for i in range(m):
    com = list(input().split())

    if len(com) > 1:
        com[1] = int(com[1])
        if com[0] == 'add':
            s[com[1]] = 1
        elif com[0] == 'remove':
            s[com[1]] = 0
        elif com[0] == 'check':
            print(int(s[com[1]] == 1))
        elif com[0] == 'toggle':
            s[com[1]] = 1 - s[com[1]]
    else:

        if com[0] == 'all':
            s = [1] * 21
        elif com[0] == 'empty':
            s = [0] * 21