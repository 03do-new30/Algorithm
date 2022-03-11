import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(N)]

# 정사각형의 한 변의 길이가 될 수 있는 최대
max_side = min(M, N)

ans = 1
for r in range(N):
    for c in range(M):
        # (r, c)가 좌측 상단 꼭짓점일 때
        # (r, c)와 나머지 세 꼭짓점이 같은 숫자인지 확인한다
        for i in range(1, max_side):
            if 0 <= r + i < N and 0 <= c + i < M:
                if arr[r][c] == arr[r+i][c] == arr[r][c+i] == arr[r+i][c+i]:
                    ans = max(ans, (i+1)*(i+1))

print(ans)
