import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
groups = 0

while n >= 2 and m >= 1:
    groups += 1
    n -= 2
    m -= 1

# print("초기 상태 - n:", n, "m:", m, "groups:", groups, "k:", k)

while k > 0:
    # print("n:", n, "m:", m, "groups:", groups, "k:", k)
    # 그룹 짓지 못한 인원 중 인턴십 인원 뽑기
    if n > 0:
        n -= 1
        k -= 1
        continue
    if m > 0:
        m -= 1
        k -= 1
        continue
    # 그룹 해체
    groups -= 1
    n += 2
    m += 1

print(groups)
