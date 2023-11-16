import sys
input = sys.stdin.readline

LIMIT = 5
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def gen(k):
    # 이동을 4진법으로 표시
    a = [0] * LIMIT
    for i in range(LIMIT):
        a[i] = k & 3
        k = k >> 2
    return a

def check(arr, dirs):
    n = len(arr)

    for dir in dirs:
        merged = [[False] * n for _ in range(n)]

        while True:
            moved = False

            if dir == 0:
                for i in range(n-2, -1, -1):
                    for j in range(n):
                        if arr[i][j] == 0:
                            continue
                        if arr[i+1][j] == 0:
                            arr[i+1][j] = arr[i][j]
                            merged[i+1][j] = merged[i][j]
                            arr[i][j] = 0
                            moved = True
                        elif arr[i+1][j] == arr[i][j]:
                            if not merged[i][j] and not merged[i+1][j]:
                                arr[i+1][j] *= 2
                                merged[i+1][j] = True
                                arr[i][j] = 0
                                moved = True
            elif dir == 1:
                for i in range(1, n):
                    for j in range(n):
                        if arr[i][j] == 0:
                            continue
                        if arr[i-1][j] == 0:
                            arr[i-1][j] = arr[i][j]
                            merged[i-1][j] = merged[i][j]
                            arr[i][j] = 0
                            moved = True
                        elif arr[i-1][j] == arr[i][j]:
                            if not merged[i-1][j] and not merged[i][j]:
                                arr[i-1][j] *= 2
                                merged[i-1][j] = True
                                arr[i][j] = 0
                                moved = True
            elif dir == 2:
                for j in range(1, n):
                    for i in range(n):
                        if arr[i][j] == 0:
                            continue
                        if arr[i][j-1] == 0:
                            arr[i][j-1] = arr[i][j]
                            merged[i][j-1] = merged[i][j]
                            arr[i][j] = 0
                            moved = True
                        elif arr[i][j-1] == arr[i][j]:
                            if not merged[i][j] and not merged[i][j-1]:
                                arr[i][j-1] *= 2
                                merged[i][j-1] = True
                                arr[i][j] = 0
                                moved = True
            elif dir == 3:
                for j in range(n-2, -1, -1):
                    for i in range(n):
                        if arr[i][j] == 0:
                            continue
                        if arr[i][j+1] == 0:
                            arr[i][j+1] = arr[i][j]
                            merged[i][j+1] = merged[i][j]
                            arr[i][j] = 0
                            moved = True
                        elif arr[i][j+1] == arr[i][j]:
                            if not merged[i][j] and not merged[i][j+1]:
                                arr[i][j+1] *= 2
                                merged[i][j+1] = True
                                arr[i][j] = 0
                                moved = True
            
            if not moved:
                break
    
    ans = max([max(row) for row in arr])
    return ans
    

n = int(input())
original = []
for _ in range(n):
    original.append(list(map(int, input().split())))

answer = 0

# 최대 5번 이동, 경우의 수는 4**5 = 2**10 = 1024
for k in range(1 << (LIMIT * 2)):
    dirs = gen(k)
    
    arr = [row[:] for row in original]

    cur = check(arr, dirs)
    if cur > answer:
        answer = cur

print(answer)