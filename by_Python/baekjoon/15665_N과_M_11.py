import sys
input = sys.stdin.readline

n, m = map(int, input().split())


### 1 ###
# 같은 수를 여러번 골라도 되므로 N과 M 9번, 10번 문제와 달리
# 각 자연수의 등장 횟수를 고려하지 않아도 된다
nums = sorted(set(map(int, input().split())))
n = len(nums)

### 2 ###
seq = [0] * m

def solve(idx):
    if idx == m:
        print(' '.join(list(map(str, seq))))
        return
    
    for num in nums:
        seq[idx] = num
        solve(idx + 1)

solve(0)