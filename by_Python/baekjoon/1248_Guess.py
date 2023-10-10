import sys
input = sys.stdin.readline

n = int(input())
s = input().strip()
sign = [[0] * n for _ in range(n)]
s_idx = 0
for i in range(n):
    for j in range(i, n):
        if s[s_idx] == '-':
            sign[i][j] = -1
        elif s[s_idx] == '+':
            sign[i][j] = 1
        else:
            sign[i][j] = 0
        s_idx += 1

seq = [0] * n
def solve(idx):
    if idx == n:
        return True
    
    if sign[idx][idx] == 0:
        seq[idx] = 0
        return check(idx) and solve(idx + 1)
    
    for num in range(1, 11):
        seq[idx] = num * sign[idx][idx]
        if check(idx) and solve(idx + 1):
            return True
    return False

def check(idx):
    sum = 0
    for i in range(idx, -1, -1):
        sum += seq[i]
        
        if sum == 0:
            if sign[i][idx] != 0:
                return False
        elif sum > 0:
            if sign[i][idx] != 1:
                return False
        else:
            if sign[i][idx] != -1:
                return False
    return True

solve(0)
print(' '.join(map(str, seq)))
