import sys
input = sys.stdin.readline

from collections import Counter

n, m = map(int, input().split())
nums = sorted(map(int, input().split()))

### 1 ###
# 입력 -> 중복되는 숫자가 등장할 수 있음
# 각 숫자가 몇번 등장하는지 카운트

tmp = dict(Counter(nums)) # tmp: {1: 1, 7: 1, 9: 2}
num, cnt = map(list, zip(*tmp.items())) # num: [1, 7, 9] # cnt: [1, 1, 2]
n = len(num)

### 2 ###
seq = [0] * m
def solve(idx):
    if idx == m:
        sys.stdout.write(' '.join(list(map(str, seq))) + '\n')
        return
    
    for i in range(n):
        if cnt[i] <= 0:
            continue

        cnt[i] -= 1
        seq[idx] = num[i]
        solve(idx + 1)
        cnt[i] += 1 # 복구

solve(0)


