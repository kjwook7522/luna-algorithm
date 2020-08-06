# input value
N = int(input())
table = []
for _ in range(N):
  table.append(list(map(int, input().split(' '))))
times = []
for _ in range(N):
  times.append([0] * N)

# def
def check(times, x, y):
  for i in range(1, 9):
    if x - i >= 0:
      if table[y][x-i] == i:
        times[y][x] += times[y][x-i]
  
  for i in range(1, 9):
    if y - i >= 0:
      if table[y-i][x] == i:
        times[y][x] += times[y-i][x]
  
  return times

# main
times[0][0] = 1
for y in range(N):
  for x in range(N):
    check(times, x, y)
print(times[N-1][N-1])