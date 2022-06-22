import sys
input=sys.stdin.readline
S=set()
for _ in range(int(input())):
    cmd=input().split()
    if len(cmd)==1:
        command=cmd[0]
        if command=='all':
            S=set(range(1,21))
        else:
            S=set()
    else:
        command=cmd[0]
        x=int(cmd[1])
        
        if command=='add':
            S.add(x)
        elif command=='remove':
            S.discard(x)
        elif command=='check':
            print(1 if x in S else 0)
        elif command=='toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)