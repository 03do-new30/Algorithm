import sys
input = sys.stdin.readline

from collections import Counter

n, m = map(int, input().split())
nums = sorted(map(int, input().split()))

### 1 ###
# 중복되는 자연수 등장 가능, 카운트 필요
tmp = dict(Counter(nums))
num, cnt = map(list, zip(*tmp.items()))

### 2 ###
# 비내림차순
seq = [0] * m
n = len(num)
def solve(idx):
    if idx == m:
        print(' '.join(list(map(str, seq))))
        return
    
    for i in range(n):
        if cnt[i] <= 0:
            continue

        if idx == 0:
            cnt[i] -= 1
            seq[idx] = num[i]
            solve(idx + 1)
            cnt[i] += 1
        else:
            if seq[idx-1] <= num[i]:
                cnt[i] -= 1
                seq[idx] = num[i]
                solve(idx + 1)
                cnt[i] += 1
solve(0)