import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
log = ''

"""
백준 해설강의 참고
"""

# 행이 홀수: RDLDR...
if n % 2 == 1:
    for i in range(n):
        if i % 2 == 0:
            log += 'R' * (m-1)
            if i != n-1:
                log += 'D'
        else:
            log += 'L' * (m-1)
            log += 'D'
# 열이 홀수: DRURD..
elif m % 2 == 1:
    for i in range(m):
        if i % 2 == 0:
            log += 'D' * (n-1)
            if i != m-1:
                log += 'R'
        else:
            log += 'U' * (n-1)
            log += 'R'
# 행과 열이 모두 짝수
else:
    # 이동하지 않을 칸을 하나 고른다
    xr = 0; xc = 1
    for r in range(n):
        for c in range(m):
            # 검정칸이면서, 칸에 써있는 수가 최소인 것
            if (r+c) % 2 == 1: # 검정칸
                if arr[xr][xc] > arr[r][c]:
                    xr = r
                    xc = c
    # print("xr:", xr, "xc:", xc)
    # A의 위치
    ar = ac = 0
    # B의 위치
    br = n-1; bc = m-1

    log2 = ""
    while br - ar > 1:
        if ar // 2 < xr // 2:
            log += 'R' * (m-1)
            log += 'D'
            log += 'L' * (m-1)
            log += 'D'
            ar += 2

        if xr // 2 < br // 2:
            log2 += 'R' * (m-1)
            log2 += 'D'
            log2 += 'L' * (m-1)
            log2 += 'D'
            br -= 2
    
    while bc - ac > 1:
        if ac // 2 < xc // 2:
            log += 'DRUR'
            ac += 2
        if xc // 2 < bc // 2:
            log2 += 'DRUR'
            bc -= 2
    
    if xc == ac:
        log += 'RD'
    else:
        log += 'DR'
    log += log2[::-1]

print(log)

