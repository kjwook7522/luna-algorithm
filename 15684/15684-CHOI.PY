from itertools import permutations
from sys import stdin

answer = int(1e9)
N, M, H = map(int, stdin.readline().split())
ladders = [[0] * (N + 1) for _ in range(H + 1)]
for _ in range(M):
    a, b = map(int, stdin.readline().split())
    ladders[a][b] = 1


def check_possible(ladder):
    for i in range(1, N + 1):
        now = i
        for j in range(1, H + 1):
            if ladder[j][now] == 1:
                now = now + 1
            elif ladder[j][now - 1] == 1 and now > 1:
                now = now - 1
        if now != i:
            return False

    return True


def DFS(cnt, ladder):
    global answer
    if cnt > 3:
        return
    if check_possible(ladder):
        answer = min(answer,cnt)
        return 
    if answer <= cnt:
        return
    elif cnt < 3:
        for i in range(1, N):
            for j in range(1, H + 1):
                if ladder[j][i + 1] == 0 and ladder[j][i - 1] == 0 and ladder[j][i] == 0:
                    ladder[j][i] = 1
                    DFS(cnt + 1, ladder)
                    ladder[j][i] = 0

    return

DFS(0, ladders)

if answer == int(1e9):
    print(-1)
else:
    print(answer)
