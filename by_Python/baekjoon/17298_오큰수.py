import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().strip().split(' ')))

### 1 ###
nge = [0] * n
idx_stack = []

for i in range(n):
    if i == 0:
        idx_stack.append(i)
        continue

    while len(idx_stack) > 0 and a[idx_stack[-1]] < a[i]:
        nge[idx_stack.pop()] = a[i]
    
    idx_stack.append(i)

### 2 ###
while idx_stack:
    nge[idx_stack.pop()] = -1

### 3 ###
nge = list(map(str, nge))
print(' '.join(nge))