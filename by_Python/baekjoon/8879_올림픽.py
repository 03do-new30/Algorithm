import sys
input = sys.stdin.readline
from collections import deque

N, K = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]
countries.sort(key = lambda x : (-x[1], -x[2], -x[3]))

# ranking[x] = ranking of country x
ranking = 0
for i in range(N):
    country = countries[i][0]
    
    if i == 0:
        ranking = 1
    else:
        if countries[i][1:] != countries[i-1][1:]:
            ranking = i + 1
    
    if country == K:
        print(ranking)
        break
