from sys import stdin
from collections import deque

def is_exception(x,y):
    global board,N
    if x > N or y > N or x < 1 or y < 1:
        return True
    if board[x][y] == 1:
        return True
    return False

move = [[0,1],[1,0],[0,-1],[-1,0]]
# 1->4 : right
# 4->1 : left
N = int(input())
K = int(input())
board = [[0]*(N+1) for _ in range(N+1)]
commands = ['']*(10000+1)
for _ in range(K):
    row,col = map(int,stdin.readline().split())
    board[row][col] = 2
L= int(input())
for _ in range(L):
    time,dir = stdin.readline().split()
    commands[int(time)] = dir


direction = 0
#     right
now_x,now_y = 1,1
tails = deque()
tails.append((1,1))
t = 0
while True:
    t += 1
    now_x += move[direction][0]
    now_y += move[direction][1]
    tail = tails.popleft()

    if is_exception(now_x,now_y):
        print(t)
        exit()
    board[tail[0]][tail[1]] = 0
    if board[now_x][now_y] == 0: # non apple
        board[now_x][now_y] = 1
    elif board[now_x][now_y] == 2: # apple
        board[now_x][now_y] = 1
        board[tail[0]][tail[1]] = 1
        tails.appendleft(tail)

    tails.append((now_x,now_y))

    if commands[t] == 'L':
        direction = (direction - 1) % 4
    elif commands[t] == 'D':
        direction = (direction + 1) % 4


