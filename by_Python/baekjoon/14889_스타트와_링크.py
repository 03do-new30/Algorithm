import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 000111처럼 팀 하나는 0, 팀 하나는 1로 해서 순열 만들기
seq = [0] * (n//2) + [1] * (n//2)

def next_permutation(seq):
    i = len(seq) - 1
    while i > 0 and seq[i-1] >= seq[i]:
        i -= 1
    if i == 0:
        return False
    
    j = len(seq) - 1
    while seq[i-1] >= seq[j]:
        j -= 1
    seq[i-1], seq[j] = seq[j], seq[i-1]

    j = len(seq) - 1
    while i < j:
        seq[i], seq[j] = seq[j], seq[i]
        i += 1
        j -= 1
    
    return True

diff = 100
while True:
    team_0 = []
    team_1 = []
    for i in range(n):
        if seq[i] == 0:
            team_0.append(i)
        else:
            team_1.append(i)
    
    stat_0 = 0
    stat_1 = 0
    for i in range(n//2 -1):
        for j in range(i+1, n//2):
            stat_0 += arr[team_0[i]][team_0[j]] + arr[team_0[j]][team_0[i]]
            stat_1 += arr[team_1[i]][team_1[j]] + arr[team_1[j]][team_1[i]]
    diff = min(diff, abs(stat_0 - stat_1))
    if not next_permutation(seq):
        break

print(diff)