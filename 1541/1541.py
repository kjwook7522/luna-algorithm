# input value
formula = input()
numbers = formula.replace('+', ',').replace('-', ',').split(',')
numbers = list(map(int, numbers))
sign = ['+']
for ch in formula:
  if ch == '+':
    sign.append('+')
  elif ch == '-':
    sign.append('-')

#def
def searchFirstMinus(signList):
  if '-' in signList:
    return signList.index('-')
  else:
    return len(signList)

#main
index = searchFirstMinus(sign)

answer = 0
for i in numbers[:index]:
  answer += i
for i in numbers[index:]:
  answer -= i

print(answer)