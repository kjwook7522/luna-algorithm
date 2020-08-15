from sys import stdin

N = int(stdin.readline())

cost = [[0] * 3 for _ in range(N + 1)]

for i in range(1, N + 1):
    R, G, B = map(int, stdin.readline().split())
    cost[i][0] = R
    cost[i][1] = G
    cost[i][2] = B

dp = [[-1] * 3 for _ in range(N + 1)]

for i in range(1, N + 1):
    if i == 1:
        dp[i][0] = cost[i][0]
        dp[i][1] = cost[i][1]
        dp[i][2] = cost[i][2]
        continue

    dp[i][0] = cost[i][0] + min(dp[i - 1][1], dp[i - 1][2])
    dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])
    dp[i][2] = cost[i][2] + min(dp[i - 1][0], dp[i - 1][1])

result = min(dp[N])
print(result)
