# input value
n, k = map(int, input().split(' '))
value = []
dp = [0 for _ in range(k+1)]
dp[0] = 1
for _ in range(n):
  value.append(int(input()))

value.sort(reverse=True)

# main
for v in value:
  for i in range(1, k+1):
    if i >= v:
      dp[i] += dp[i-v]

print(dp[k])