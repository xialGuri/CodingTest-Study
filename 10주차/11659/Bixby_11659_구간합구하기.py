n,m=map(int,input().split())
numbers=list(map(int,input().split()))
prefixsum=[0]*(n+1)
for i in range(n):
    prefixsum[i+1]=prefixsum[i]+numbers[i]
for i in range(m):
    a,b=map(int,input().split())
    print(prefixsum[b]-prefixsum[a-1])
