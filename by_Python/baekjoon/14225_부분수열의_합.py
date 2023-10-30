import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

# 비트마스크로 풀이
# 합 저장
sums = set()

for i in range(1, 1 << n):
    total = 0 # 합 저장
    # j번째 수가 부분집합 i에 포함되는지 확인한다
    for j in range(n):
        if i & (1 << j) > 0:
            total += s[j]
    
    sums.add(total)

# 수열 s의 부분 수열의 합으로 나올 수 없는 가장 작은 자연수를 구한다
sums = sorted(list(sums))

found = False
target = 1
for num in sums:
    if num == target:
        target += 1
    else:
        print(target)
        found = True
        break

if not found:
    print(target)