import sys
input = sys.stdin.readline

n = int(input().strip())
g = [list(map(int, input().split())) for _ in range(n)]

# Floyd Warshall
# i -> k번 노드 -> j 로 거쳐가는 경로를 확인한다
for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1 or (g[i][k] == 1 and g[k][j] == 1):
                g[i][j] = 1
                """
                어차피 g[i][j] = 1로 갱신하기 때문에
                사실 g[i][j] == 1인 경우는 검사 안하고 넘어가도 됨
                그러나 이해를 위해 if문에서 검사하기로!
                """

# 출력
for row in g:
    for x in row:
        print(x, end=' ')
    print()
