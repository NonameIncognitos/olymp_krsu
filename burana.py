from collections import deque

n = int(input())
numbers = list(map(int, input().split()))

visit = []
mp = {}
for i in range(n):
    x = numbers[i]
    mp[x] = mp.get(x, 0) + 1
    for j in range(100):
        visit.append(x + j)

visit = sorted(set(visit))

time = 0
al_time = 0
dq = deque()
used = {}
while mp or al_time > 0:
    if visit[time] in mp:
        al_time += mp[visit[time]]
        mp.pop(visit[time])

    time += 1
    if dq and dq[0] == visit[time]:
        dq.popleft()

    if visit[time] in used:
        continue

    if al_time and len(dq) < 5:
        al_time -= 1
        used[visit[time] + 6] = 1
        dq.append(visit[time] + 6)

print(visit[time] + 6)

