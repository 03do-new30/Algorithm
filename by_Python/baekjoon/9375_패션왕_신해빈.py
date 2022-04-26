# 출처: https://donggoolosori.github.io/2020/10/05/boj-9375/

import sys
input = sys.stdin.readline
from collections import defaultdict
from itertools import combinations

for _ in range(int(input())):
    n = int(input())
    clothes = defaultdict(int)
    for __ in range(n):
        x, category = input().split()
        clothes[category] += 1
    
    # (의상의 종류 + 의상을 입지 않은 경우의 수) 모두 곱해주고, 모두 안 입은 경우의 수 1을 빼준다
    ans = 1
    for x in clothes:
        ans *= (clothes[x] + 1)
    ans -= 1

    print(ans)

