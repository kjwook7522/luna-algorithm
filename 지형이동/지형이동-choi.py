import math
from collections import deque, defaultdict
import sys
sys.setrecursionlimit(10**6)

def bfs(reg, land, start, height, cnt):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    reg[start[0]][start[1]] = cnt
    q = deque([start])
    n = len(land)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                h = abs(land[x][y] - land[nx][ny])
                if reg[nx][ny] == 0 and h <= height:
                    reg[nx][ny] = cnt
                    q.append([nx, ny])


def find_ladder(land, region):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visit = defaultdict(lambda: math.inf)
    n = len(land)
    for i in range(n):
        for j in range(n):
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    if region[i][j] != region[nx][ny]:
                        reg1 = region[i][j]
                        reg2 = region[nx][ny]
                        dif = abs(land[i][j] - land[nx][ny])
                        visit[(reg1, reg2)] = min(visit[(reg1, reg2)], dif)

    return visit


def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])

    return parent[a]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[a] = b
    elif a < b:
        parent[b] = a


def solution(land, height):
    answer = 0
    n = len(land)
    region = [[0] * (n) for _ in range(n)]
    cnt = 1

    for i in range(n):
        for j in range(n):
            if region[i][j] == 0:
                bfs(region, land, [i, j], height, cnt)
                cnt += 1

    visit = find_ladder(land,region)
    visit = sorted(visit.items(),key=lambda x: x[1])
    parent = {i:i for i in range(1,cnt)}
    for (x,y),val in visit:
        if find_parent(parent,x) != find_parent(parent,y):
            union_parent(parent,x,y)
            answer += val
        if len(parent.values()) == 1:
            break
    
    return answer
