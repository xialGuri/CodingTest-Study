n,k=map(int,input().split())
W=[]
V=[]
dp=[[0]*(k+1)for _ in range(n+1)]
for i in range(n):
    weight,value=map(int,input().split())
    W.append(weight)
    V.append(value)

for i in range(1,n+1):
    for j in range(1,k+1):
        if j<W[i-1]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-W[i-1]]+V[i-1])
print(dp[n][k])