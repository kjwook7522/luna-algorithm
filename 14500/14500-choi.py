from sys import stdin

def cal_sum(r, c, t):  # 해당 tetromino 의 좌표들
    summ = 0
    global N, M
    for dx, dy in t:
        nx = r + dx
        ny = c + dy
        if 0 <= nx < N and 0 <= ny < M:
            summ += board[nx][ny]
        else:
            return -1
    return summ


N, M = map(int, stdin.readline().split())
board = []
for n in range(N):
    board.append(list(map(int, stdin.readline().split(' '))))
ans = 0

tetrominos = [([0, 0], [0, 1], [0, 2], [0, 3]),  # ----
              ([0, 0], [1, 0], [2, 0], [3, 0]),
              ([0, 0], [0, 1], [1, 1], [1, 0]),  # ㅁ
              ([0, 0], [1, 0], [1, 1], [1, 2]),  # ㄴ
              ([0, 0], [0, 1], [1, 0], [2, 0]),
              ([0, 0], [0, 1], [0, 2], [1, 2]),
              ([0, 1], [1, 1], [2, 1], [2, 0]),
              ([0, 0], [0, 1], [1, 1], [2, 1]),
              ([1, 0], [1, 1], [1, 2], [0, 2]),
              ([0, 0], [1, 0], [2, 0], [2, 1]),
              ([0, 0], [1, 0], [0, 1], [0, 2]),
              #
              ##
              #
              ([0, 0], [1, 0], [1, 1], [2, 1]),  # 번개
              ([1, 0], [1, 1], [0, 1], [0, 2]),

              #
              ##
              #
              ([2, 0], [1, 0], [1, 1], [0, 1]),
              ([0, 0], [0, 1], [1, 1], [1, 2]),

              ([0, 0], [0, 1], [1, 1], [0, 2]),  # ㅜ
              ([1, 0], [0, 1], [1, 1], [2, 1]),
              ([1, 0], [1, 1], [1, 2], [0, 1]),
              ([0, 0], [1, 0], [1, 1], [2, 0])]

max_sum = 0

for r in range(N):
    for c in range(M):
        for tetromino in tetrominos:
            max_sum = max(max_sum, cal_sum(r, c, tetromino))

# edge-case : 4*500*4*5*4 = 2000 * 16 * 5 = 160000번 연산
print(max_sum)
