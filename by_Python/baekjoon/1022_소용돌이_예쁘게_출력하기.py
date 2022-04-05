import sys
input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().split())
n = r2 - r1 + 1
m = c2 - c1 + 1

# (r1, c1) ~ (r2, c2)까지의 모눈종이
arr = [[0]*m for _ in range(n)]

# r1, c1, r2, c2 중 절대값이 가장 큰 것을 찾는다
biggest = max(map(abs, [r1, c1, r2, c2]))

# 좌표 (r, c)를 반시계방향으로 움직이며 값을 +1씩 해준다.
# 0(0,0)~(0,0)에서부터 biggest(biggest-1, biggest) ~ (biggest, biggest)단계까지 값을 조작하되, 
# 메모리 초과 방지를 위해 (r1, c1) ~(r2, c2) 영역 내에 좌표 (r, c)가 있을 때만 arr[r][c]에 그 값ㅇ르 기록한다.

# 반시계방향
dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]
# 단계를 나타내는 step 및 좌표 (r, c)의 초기값 설정
step = 0
r = c = step
val = 1
while step <= biggest:
    if step == 0:
        # 범위 확인
        if r1 <= r <= r2 and c1 <= c <= c2:
            arr[r-r1][c-c1] = val
    else:
        r, c = step-1, step
        val += 1
        for i in range(4):
            while -step <= r + dr[i] <= step and -step <= c + dc[i] <= step:
                # 범위 확인
                if r1 <= r <= r2 and c1 <= c <= c2:
                    arr[r-r1][c-c1] = val
                # update
                r += dr[i]
                c += dc[i]
                val += 1
        # (step, step) 채워주기
        if r1 <= step <= r2 and c1 <= step <= c2:
            arr[step-r1][step-c1] = val

    step += 1

# 출력
# 가장 큰 숫자의 길이
max_val = max(arr[0][0], arr[0][m-1], arr[n-1][0], arr[n-1][m-1])
max_len = len(str(max_val))

for i in range(n):
    for j in range(m):
        print(str(arr[i][j]).rjust(max_len), end = ' ')
    print()