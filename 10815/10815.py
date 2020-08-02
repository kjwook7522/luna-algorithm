# input
N = int(input())
Narray = list(map(int, input().split(' ')))
M = int(input())
Marray = list(map(int, input().split(' ')))

# def
def binarySearch(target, left, right):
  if left > right:
    return 0
  
  mid = (left + right) // 2
  
  if Narray[mid] == target:
    return 1
  elif Narray[mid] > target:
    return binarySearch(target, left, mid-1)
  elif Narray[mid] < target:
    return binarySearch(target, mid+1, right)
  else:
    return 0

# main
Narray.sort()
left = 0
right = N-1
answer = [0 for i in range(M)]

for i, value in enumerate(Marray):
  answer[i] = binarySearch(value,left, right)

print(' '.join(map(str, answer)))