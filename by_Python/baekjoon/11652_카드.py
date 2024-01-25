import sys
input = sys.stdin.readline

n = int(input())
cards = dict()

for _ in range(n):
    num = int(input())
    if num in cards:
        cards[num] += 1
    else:
        cards[num] = 1

# 가장 많은 카드의 개수
max_val = max(cards.values())
# 가장 많은 카드 개수 조건을 충족하는 key들 중 가장 작은 정수 찾는다
keys = list(cards.keys())
keys.sort()
for k in keys:
    if cards[k] == max_val:
        print(k)
        break