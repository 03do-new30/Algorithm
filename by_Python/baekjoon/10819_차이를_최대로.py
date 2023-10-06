import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

# 주어진 정수들로 순열을 만들어보며 하나하나 최댓값 구함
# N! = 8! = 40320
# N * N!
ans = -100
seq = [0] * n
visited = [False] * n
def solve(idx):
    global ans

    if idx == n:
        tmp = 0
        for i in range(n-1):
            tmp += abs(seq[i] - seq[i+1])
        
        if ans < tmp:
            ans = tmp
        return
    
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        seq[idx] = a[i]
        solve(idx + 1)
        visited[i] = False

solve(0)
print(ans)