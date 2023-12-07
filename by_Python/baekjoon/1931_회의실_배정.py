import sys
input = sys.stdin.readline

n = int(input())
by_total = dict()
for _ in range(n):
    start, end = map(int, input().split())
    total = end - start
    if total in by_total:
        by_total[total].append((start, end))
    else:
        by_total[total] = [(start, end)]
print(by_total)

for total in sorted(by_total.keys()):
    print(by_total[total])