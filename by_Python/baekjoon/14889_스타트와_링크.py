import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def next_permutation(a):
    i = len(a) - 1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i == 0:
        return False
    
    j = len(a) - 1
    while a[j] <= a[i-1]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]

    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
    return True

def stat(team):
    ret = 0
    for i in range(len(team) -1):
        for j in range(i+1, len(team)):
            x = team[i]
            y = team[j]
            ret += arr[x][y] + arr[y][x]
    return ret

seq = [0] * (n//2) + [1] * (n//2)
answer = 1000000
while True:
    team_a = []
    team_b = []
    for i in range(n):
        if seq[i] == 0:
            team_a.append(i)
        else:
            team_b.append(i)
    # print("team_a:", team_a, "team_b:", team_b)
    stat_a = stat(team_a)
    stat_b = stat(team_b)
    # print("stat_a:", stat_a, "stat_b:", stat_b)
    diff = abs(stat_a - stat_b)
    answer = min(answer, diff)
    if answer == 0:
        break
    if not next_permutation(seq):
        break
print(answer)