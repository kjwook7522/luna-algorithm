from collections import deque
from sys import stdin

wheels = []
visited = [False]*4
LEFT, RIGHT = 6,2
for i in range(4):
    w = input().rstrip()
    wheels.append(deque())
    for idx in range(len(w)):
        wheels[i].append(int(w[idx]))

K = int(input())


def roll_wheel(wheels, index, dir):
    var = 0
    if dir == -1:
        var = wheels[index].popleft()
        wheels[index].append(var)
    else:
        var = wheels[index].pop()
        wheels[index].appendleft(var)
    return


def do_wheels(wheels, start, dir, visited):
    if 0 <= start < 4:
        if not visited[start]:
            l = wheels[start][LEFT]
            r = wheels[start][RIGHT]
            roll_wheel(wheels, start, dir)
            visited[start] = True
            if start != 0:
                if l != wheels[start-1][RIGHT]:
                    do_wheels(wheels,start-1,-dir,visited)
            if start != 3:
                if r != wheels[start+1][LEFT]:
                    do_wheels(wheels,start+1,-dir,visited)
    visited[start] = False

for k in range(K):
    start, dir = map(int, stdin.readline().split())
    do_wheels(wheels, start-1, dir, visited)

ans = 0
score = [1,2,4,8]
for j in range(4):
    if wheels[j][0] == 1:
        ans += score[j]

print(ans)
