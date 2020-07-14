# input values
origin = []
change = []
M, N = input().split(" ")
M = int(M)
N = int(N)
for i in range(M):
  origin.append(list(map(int, input())))
for i in range(M):
  change.append(list(map(int, input())))

#def
def search(ori, chg, M, N):
  times = 0
  for i in range(M-2):
    for j in range(N-2):
      if ori[i][j] != chg[i][j]:
        swap3x3(ori, i, j)
        times += 1
    if not cmpLine(ori, chg, i):
      return -1
  
  if not cmpLine(ori, chg, M-2):
    return -1
  if not cmpLine(ori, chg, M-1):
    return -1
  
  return times

def swap(array, i, j):
  if array[i][j] == 1:
    array[i][j] = 0
  elif array[i][j] == 0:
    array[i][j] = 1
  else:
    print("swap: wrong value error in array[i][j]")

def swap3x3(array, i, j):
  swap(array, i, j)
  swap(array, i, j+1)
  swap(array, i, j+2)
  swap(array, i+1, j)
  swap(array, i+1, j+1)
  swap(array, i+1, j+2)
  swap(array, i+2, j)
  swap(array, i+2, j+1)
  swap(array, i+2, j+2)

def cmpLine(ori, chg, line):
  if ori[line] == chg[line]:
    return True
  else:
    return False

# main
answer = search(origin, change, M, N)
print(answer)
