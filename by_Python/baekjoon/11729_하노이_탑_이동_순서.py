import sys
input = sys.stdin.readline

n = int(input())

# n개의 원판(1~n 디스크)을 x번탑 -> y번탑으로 이동시키는 함수
count = 0
logs = []
def solve(n, x, y):
    global count

    if n == 0:
        return

    # 1 ~ n-1 디스크를 z번 탑으로 이동시킨다
    z = 0
    if x != 1 and y != 1:
        z = 1
    elif x != 2 and y != 2:
        z = 2
    elif x != 3 and y != 3:
        z = 3
    solve(n-1, x, z)
    # 크기가 n인 디스크를 x번 탑 -> y번 탑으로 이동시킨다
    count += 1
    print(x, y)
    
    # 1 ~ n-1 디스크를 y번 탑으로 이동시킨다
    solve(n-1, z, y)

# 최소 이동 횟수 구하기
# D[1] = 1
# D[N] = D[N-1] + 1 + D[N-1]
#      = 2*D[N-1] + 1
# D[N] + 1 = 2*D[N-1] + 2
#          = 2(D[N-1] + 1)
# 위를 통해 일반항을 구하면
# E[N] = 2E[N-1]
# 우리는 D[1] = 1 을 이용해 E[1] = 2라는 사실을 안다
# E[N] = 2 ** N
# D[N] + 1 = 2 ** N
# D[N] = 2 ** N - 1
print(2 ** n - 1)
# 함수 호출
solve(n, 1, 3)
