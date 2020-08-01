# input value
N = int(input())

# def
def subOne(n, array):
  array[n-2] = True
  return

def divTwo(n, array):

  if n % 2 == 0:
    array[int(n/2) - 1] = True
    
  return

def divThree(n, array):
  if n % 3 == 0:
    array[int(n/3) - 1] = True
    
  return

# main
answer = 0
array = [False for i in range(N)]
array[N-1] = True

while True:
  if array[0] == True:
    break
  
  newArray = [False for i in range(N)]
  for n in range(len(array)):
    if array[n] == True:
      subOne(n+1, newArray)
      divTwo(n+1, newArray)
      divThree(n+1, newArray)
  
  array = newArray
  answer += 1
  
print(answer)