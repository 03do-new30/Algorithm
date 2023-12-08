import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, list(input().strip()))) for _ in range(n)]
b = [list(map(int, list(input().strip()))) for _ in range(n)]

def convert(r, c):
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            a[i][j] = (a[i][j] + 1) % 2

ans = 0
for r in range(n-2):
    for c in range(m-2):
        # 3*3 부분행렬의 왼쪽상단 꼭지점을 기준으로
        # 행렬을 변환하는 연산 실시 여부 판단
        if a[r][c] != b[r][c]:
            convert(r, c)
            ans += 1

# 행렬이 같은지 판단
for r in range(n):
    for c in range(m):
        if a[r][c] != b[r][c]:
            ans = -1
            break

print(ans)