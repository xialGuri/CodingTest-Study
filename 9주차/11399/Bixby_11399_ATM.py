n=int(input())
p=sorted(list(map(int,input().split())))
answer=0
for i in range(n):
    answer+=sum(p[0:i+1])
print(answer)