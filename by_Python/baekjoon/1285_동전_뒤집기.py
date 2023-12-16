import sys
input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]

def flip(x):
    if x == 'H':
        return 'T'
    return 'H'

# 2**(2N) 가지 방법이 존재 -> 2**40 -> BruteForce 불가능

# 행 뒤집기를 고정해놓고, 그 뒤에 열 뒤집기를 하는 방법은?
# 행 뒤집기는 2**N -> 2**20 -> 1048576, BruteForce 가능

# 행 뒤집기
min_tail = n * n
for state in range(1 << n): # 비트마스크로 행 뒤집는 경우 구성
    total = 0
    for c in range(n):
        cnt = 0
        for r in range(n):
            current = arr[r][c]
            if (state & (1 << r)) != 0: # r번째 행을 뒤집는 경우
                current = flip(current)
            if current == 'T':
                cnt += 1
        # T와 H의 개수를 세고, 더 적은 것을 total에 더해주면 된다
        # 우리는 늘 열을 뒤집는 행동을 할 때, T를 H보다 적게 바꿔버릴 것이므로
        total += min(cnt, n - cnt)
    
    min_tail = min(min_tail, total)
    
print(min_tail)