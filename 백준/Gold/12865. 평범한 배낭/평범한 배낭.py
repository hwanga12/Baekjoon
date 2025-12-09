N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [-1] * (K + 1)
dp[0] = 0

for P, Q in items:
    for cur in range(K, P - 1, -1):
        if dp[cur - P] != -1:
            dp[cur] = max(dp[cur], dp[cur - P] + Q)

print(max(dp))
