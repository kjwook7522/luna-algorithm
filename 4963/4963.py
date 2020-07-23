import sys
sys.setrecursionlimit(10000)

# def
def searchLand(x, y):
  if land[y][x] == 0:
    return 0
  
  goOneBlock(x, y)
  return 1

def goOneBlock(x, y):
  if x < 0 or y < 0 or x >= w or y >= h:
    return
  
  if land[y][x] == 0:
    return

  land[y][x] = 0

  goOneBlock(x+1, y)
  goOneBlock(x+1, y+1)
  goOneBlock(x, y+1)
  goOneBlock(x-1, y+1)
  goOneBlock(x-1, y)
  goOneBlock(x-1, y-1)
  goOneBlock(x, y-1)
  goOneBlock(x+1, y-1)
  return
  

# main
def main():
  if not land:
    return
  
  answer = 0
  
  for row in range(h):
    for col in range(w):
      answer += searchLand(col, row)
  
  answerList.append(answer)

# input value
w = 1
h = 1
answerList = []
while not(w == 0 and h == 0):
  land = []
  w, h = map(int ,input().split(' '))
  for i in range(h):
    row = list(map(int, input().split(' ')))
    land.append(row)
  
  main()

for n in answerList:
  print(n)