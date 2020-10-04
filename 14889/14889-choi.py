from sys import stdin
from itertools import combinations

N = int(stdin.readline())

board = [list(map(int, stdin.readline().split())) for _ in range(N)]
members = set(i for i in range(N))

def cal_sum(team):
    power = 0
    for i, j in set(combinations(team, 2)):
        power += board[i][j] + board[j][i]

    return power


min_diff = 2000  # 차이가 최대 2000 미만이므로
for team_a in set(combinations(members, N // 2)):
    team_b = members.difference(team_a)
    power_a = cal_sum(team_a)
    power_b = cal_sum(team_b)
    min_diff = min(min_diff, abs(power_a - power_b))

print(min_diff)
