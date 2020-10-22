from sys import stdin
from copy import deepcopy

l,c = map(int,stdin.readline().split())
alps = list(map(str,stdin.readline().split()))
alps.sort()
moeum = ['a','e','i','o','u']

visited = [0]*c

def DFS(now,cnt,cypher,z,m):
    if cnt == l:
        if z >= 2 and m >= 1:
            print(''.join([str(ch) for ch in cypher]))
    else:
        for i in range(now+1,c):
            if not visited[i]:
                visited[i] = 1
                cy = deepcopy(cypher)
                cy.append(alps[i])
                if alps[i] in moeum:
                    DFS(i,cnt + 1, cy,z,m+1)
                else:
                    DFS(i,cnt + 1, cy, z+1, m)
                visited[i] = 0

DFS(-1,0,[],0,0)

