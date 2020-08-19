from sys import stdin

INF = int(1e9)
N,M = map(int,stdin.readline().split())

dist = [[INF] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    dist[i][i] = 0

for i in range(M):
    n1,n2 = map(int,stdin.readline().split())
    dist[n1][n2] = 1
    dist[n2][n1] = 1

# 플로이드 워셜

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

minval = INF
for i in range(1,N+1):
    if sum(dist[i]) - INF < minval:
        minval = sum(dist[i]) - INF
        min_index = i

print(min_index)
