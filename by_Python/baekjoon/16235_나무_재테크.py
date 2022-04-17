# 참고: https://pacific-ocean.tistory.com/376
import sys
input = sys.stdin.readline
from collections import deque

# 봄, 여름
def ss():
    for r in range(N):
        for c in range(N):
            len_ = len(trees[r][c])
            for i in range(len_):
                # 봄
                if ground[r][c] - trees[r][c][i] >= 0:
                    ground[r][c] -= trees[r][c][i]
                    trees[r][c][i] += 1
                else:
                    # 오름차순이므로, 양분이 부족해지는 i부터 끝까지 다 양분이 부족할 것!
                    # 여름
                    for _ in range(i, len_):
                        ground[r][c] += trees[r][c].pop()//2
                    break

# 가을, 겨울
def fw():
    for r in range(N):
        for c in range(N):
            len_ = len(trees[r][c])
            # 가을
            for i in range(len_):
                if trees[r][c][i] % 5 == 0:
                    for j in range(8):
                        nr = r + dr[j]
                        nc = c + dc[j]
                        if 0 <= nr < N and 0 <= nc < N:
                            # 오름차순을 유지하기 위해 앞쪽에 추가
                            trees[nr][nc].appendleft(1)
            # 겨울
            ground[r][c] += A[r][c]
            

N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
trees = [[deque([]) for _ in range(N)] for _ in range(N)]

# 입력으로 주어지는 나무의 위치는 모두 서로 다름 -> 따로 정렬 필요 없이 가을에 새로 생긴 나무는 큐의 앞쪽에 넣어주는 방식으로 오름차순을 유지할 수 있다!
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

ground = [[5]*N for _ in range(N)]

# 나무 번식 방향
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(K):
    ss()
    fw()

# trees에 남아있는 나무의 개수 출력
ans = 0
for r in range(N):
    for c in range(N):
        ans += len(trees[r][c])
print(ans)