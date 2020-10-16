from collections import deque
from copy import deepcopy
dx = [-1,0,1,0]
dy = [0,1,0,-1]
board = []

for _ in range(3):
    board.append(list(map(int,input().split(' '))))

for i in range(3):
    for j in range(3):
        if board[i][j] == 0:
            start = (i, j)
            board[i][j] = 9





def make_str(arr):
    li = []
    for i in range(3):
        for j in range(3):
           li.append(str(arr[i][j]))
    return  int(''.join(li))

def BFS():
    visited = dict()
    visited[make_str(board)] = 1
    q = deque([(board, start, 0)])
    while q:
        b,s,cnt = q.popleft()
        if make_str(b) == 123456789:
            return cnt
        else:
            zx,zy = s
            for i in range(4):
                temp = deepcopy(b)
                nx = zx+dx[i]
                ny = zy+dy[i]
                if 0 <= nx < 3 and 0 <= ny < 3:
                    temp[zx][zy],temp[nx][ny] = temp[nx][ny],temp[zx][zy]
                    str_code = make_str(temp)
                    if not visited.get(str_code):
                        visited[str_code] = cnt + 1
                        q.append((temp,(nx,ny),cnt+1))

    return -1

print(BFS())


