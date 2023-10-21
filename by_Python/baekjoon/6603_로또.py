import sys
input = sys.stdin.readline

# idx = 현재 바라보고 있는 s의 인덱스
def solve(idx, lotto):
    if len(lotto) == 6:
        print(' '.join(list(map(str, lotto))))
        return
            
    for i in range(idx, k):
        if not visited[i]:
            visited[i] = True
            solve(i, lotto + [s[i]])
            visited[i] = False

while True:
    inp = list(map(int, input().split()))
    k = inp[0]
    
    if k == 0:
        break
    
    s = inp[1:]
    visited = [False] * k
    solve(0, [])
    print()
