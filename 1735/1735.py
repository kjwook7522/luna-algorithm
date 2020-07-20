# input value
numaratorA, denominatorA = list(map(int, input().split(' ')))
numaratorB, denominatorB = list(map(int, input().split(' ')))

# def
def getLCM(n, m):
  for mul in range(1, n+1):
    if (m * mul) % n == 0:
      return m * mul
  return -1

def getGCD(n, m):
  if m == 0:
    return n
  else:
    return getGCD(m, n % m)

def makeIrreducible(num, den):
  GCD = getGCD(num, den)
  num //= GCD
  den //= GCD
  return [num, den] 

# main
denLCM = getLCM(denominatorA, denominatorB)
sumNum = (numaratorA * (denLCM // denominatorA)) + (numaratorB * (denLCM // denominatorB))

answerNum, answerDen = makeIrreducible(sumNum, denLCM)
print(answerNum, answerDen)