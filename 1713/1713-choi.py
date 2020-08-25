
N = int(stdin.readline().rstrip())
num_vote = int(stdin.readline().rstrip())

votes = list(map(int, stdin.readline().split()))

q = []


def is_cand(vote):
    for member in q:
        if member[2] == vote:
            return True

    return False


for time, vote in enumerate(votes):
    if is_cand(vote):
        for i, cand in enumerate(q):
            if cand[2] == vote:
                cand[0] += 1
                break
    else:
        member_num = len(q)
        if member_num < N:
            q.append([1, time, vote])
        else:
            q[0] = [1, time, vote]
    q.sort(key=lambda x: (x[0], x[1]))


q.sort(key= lambda x: x[2])
for i in range(len(q)):
    if i == N - 1:
        print(q[i][2])
    else:
        print(q[i][2], end=' ')
