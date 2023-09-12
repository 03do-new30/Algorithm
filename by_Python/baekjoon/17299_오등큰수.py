import sys
input = sys.stdin.readline

### 0 ###
n = int(input())
a = list(map(int, input().split(' ')))

### 1 ###
# 수열의 등장 횟수를 센다
freq = dict()
for num in a:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

### 2 ### 
# 스택을 활용하여 오등큰수를 구한다
ngf = [0] * n
idx_stack = []

for i in range(n):
    if i == 0:
        idx_stack.append(i)
        continue

    while len(idx_stack) > 0 and freq[a[idx_stack[-1]]] < freq[a[i]]:
        ngf[idx_stack.pop()] = a[i]
    
    idx_stack.append(i)

### 3 ### 
# 스택에 남아 있는 인덱스 -> 오등큰수 -1
while len(idx_stack) > 0:
    ngf[idx_stack.pop()] = -1

ngf = list(map(str, ngf))
print(' '.join(ngf)) 