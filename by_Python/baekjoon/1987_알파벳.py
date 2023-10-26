import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(input().strip()))

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
check = [False] * 26

def solve(r, c, count):

    no_way = True
    for x, y in dirs:
        nr = r + x
        nc = c + y
        if 0 <= nr < n and 0 <= nc < m:
            letter = arr[nr][nc]
            if check[ord(letter) - 65]:
                continue
            no_way = False
            check[ord(letter) - 65] = True
            solve(nr, nc, count + 1)
            check[ord(letter) - 65] = False
    
    if no_way:
        global answer
        answer = max(answer, count)

answer = 0
check[ord(arr[0][0]) - 65] = True
solve(0, 0, 1)
print(answer)