from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
r, c, d = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 0 북 1 동 2 남 3 서 (절대)
q = deque()
q.append((r, c, d, 2))  # r c d count청소
ans = 0
while q:
    x, y, dir, count = q.popleft()
    next_d = dir
    flag = False
    if board[x][y] == 0:
        board[x][y] = count
    for _ in range(4):
        next_d = (next_d-1) % 4
        nx = x + dx[next_d]
        ny = y + dy[next_d]
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
            q.append((nx, ny, next_d, count + 1))
            flag = True
            break

    if not flag:
        backward_dir = (dir - 2) % 4
        bx = x + dx[backward_dir]
        by = y + dy[backward_dir]

        if board[bx][by] != 1 and 0 < bx < N-1 and 0 < by < M-1:
            q.append((bx, by, dir, count))

    ans = count -1

print(ans)
