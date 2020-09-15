from sys import stdin

n, m, x, y, k = map(int, stdin.readline().split())
board = [list(map(int, stdin.readline().split())) for _ in range(n)]
commands = list(map(int, stdin.readline().split()))

answer = []
dice = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


def roll(command, board, dice, now_x, now_y):
    nx = now_x + dx[command]
    ny = now_y + dy[command]
    if 0 <= nx < n and 0 <= ny < m:
        if command == 1:  # 동

            dice[1][1], dice[1][2], dice[3][1], dice[1][0] = dice[1][0], dice[1][1], dice[1][2], dice[3][1]
            print(dice[1][1])

        elif command == 2:  # 서
            dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]
            print(dice[1][1])

        elif command == 3:  # 북

            dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]
            print(dice[1][1])

        elif command == 4:  # 남
            dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]
            print(dice[1][1])

        if board[nx][ny] == 0:
            board[nx][ny] = dice[3][1]

        else:
            dice[3][1] = board[nx][ny]
            board[nx][ny] = 0

        return nx, ny

    else:
        return now_x, now_y


for i in range(k):
    x, y = roll(commands[i], board, dice, x, y)
