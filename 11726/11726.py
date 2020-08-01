# input value
n = int(input())

#def
def pac(n):
  if n < 1:
    return 0
  value = 1
  for i in range(1, n+1):
    value *= i
  return value

def comb(n, m):
  if n < m:
    return 0
  elif n == m or m == 0:
    return 1
  
  return (pac(n)//pac(n-m))//pac(m)

# main
answer = 0
for x2 in range(n//2 + 1):
  x1 = n - x2 * 2
  answer += comb(x1 + x2, x1)

print(answer%10007)