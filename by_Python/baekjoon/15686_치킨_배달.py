import itertools
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]


def get_chicken_dist(r1, c1, r2, c2):
    # 치킨 거리 = 집과 가장 가까운 치킨집 사이의 거리 = |r1-r2| + |c1-c2|
    return abs(r1-r2) + abs(c1-c2)


# 집과 치킨집의 좌표를 추출
home = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append((i, j))
            continue
        if city[i][j] == 2:
            chicken.append((i, j))

# m개의 치킨집 조합을 구성
combis = list(itertools.combinations(chicken, m))

ans = 1000000

# 치킨집을 combi 조합으로 남겨놓았을 때, 도시 전체의 치킨거리
for combi in combis:
    # 도시의 치킨 거리 = 모든 집의 치킨 거리의 합
    city_dist = 0
    # 각 집에서의 치킨거리
    for target_home in home:
        tmp_dist = 1000000
        for j in range(m):
            # 가장 가까운 치킨집까지의 거리
            tmp_dist = min(tmp_dist, get_chicken_dist(
                target_home[0], target_home[1], combi[j][0], combi[j][1]))
        # city_dist에 target_home의 치킨거리 더함
        city_dist += tmp_dist

    ans = min(ans, city_dist)

print(ans)
