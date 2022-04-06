import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

# time[x] = x까지오는데 걸린 시간 저장
# prev[x] = x에 오기 전 y 저장
def bfs():
    q = deque([N])
    time = [-1]*100001
    prev = [-1]*100001
    time[N] = 0
    prev[N] = None # 시작하는 N은 None으로 저장한다

    while q:
        x = q.popleft()
        # 도달
        if x == K:
            print(time[x])
            path = find_path(x, prev)
            print(' '.join(map(str, path)))
            return

        # X-1
        if 0 <= x-1 and time[x-1] == -1:
            time[x-1] = time[x] + 1
            prev[x-1] = x
            q.append(x-1)
        # X+1
        if x + 1 <= 100000 and time[x+1] == -1:
            time[x+1] = time[x] + 1
            prev[x+1] = x
            q.append(x+1)
        # 2*X
        if x*2 <= 100000 and time[x*2] == -1:
            time[x*2] = time[x] + 1
            prev[x*2] = x
            q.append(x*2)

def find_path(x, prev):
    # x까지 도달하는 데 거쳐온 위치들을 구한다
    path = []
    while True:
        if x is None:
            return reversed(path)
        path.append(x)
        x = prev[x]


# 함수 실행
bfs()