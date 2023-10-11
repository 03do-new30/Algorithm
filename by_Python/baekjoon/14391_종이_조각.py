import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input().strip() for _ in range(n)]

answer = 0

# status = 비트마스크로 종이조각을 자르는 경우를 표현
# 가로로 자르는 경우 = 0
# 세로로 자르는 경우 = 1
# arr[i][j]가 가로로 잘린다면 현재 status에서
# status & (1 << (m*i + j)) = 0이어야 한다
# arr[i][j]가 세로로 잘린다면 현재 status에서
# status & (1 << (m*i + j)) > 0이어야 한다
for status in range((1 << (n*m))):
    total = 0
    # 가로로 자르는 경우
    for i in range(n):
        garo = ""
        for j in range(m):
            if status & 1 << (i*m + j) == 0: # 가로
                garo += arr[i][j]
            else: # 세로
                if len(garo) > 0:
                    total += int(garo)
                    garo = "" # 초기화
        # 가로가 남아있는 경우
        if len(garo) > 0:
            total += int(garo)
    # 세로로 자르는 경우
    for j in range(m):
        sero = ""
        for i in range(n):
            if status & 1 << (i*m + j) > 0: # 세로
                sero += arr[i][j]
            else: # 가로
                if len(sero) > 0:
                    total += int(sero)
                    sero = "" # 초기화
        # 세로가 남아있는 경우
        if len(sero) > 0:
            total += int(sero)
    answer = max(answer, total)

print(answer)