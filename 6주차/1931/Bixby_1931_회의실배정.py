n=int(input())
meetings=sorted([list(map(int,input().split())) for _ in range(n)], key=lambda x:(x[1],x[0]))

cnt=0
endTime=-1
for i in range(n):
    if meetings[i][0]>=endTime:
        endTime=meetings[i][1]
        cnt+=1
print(cnt)