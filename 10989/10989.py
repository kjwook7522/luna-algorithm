from sys import stdin,stdout

count = [0]*10001
N = int(stdin.readline())
for i in range(N):
    count[int(stdin.readline())] += 1

for i in range(1,10001):
    for j in range(count[i]):
        stdout.write(str(i)+"\n")
