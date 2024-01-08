import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# a: A의 개수
# b: B의 개수
# a + b = n
# a * b >= k

# a + b = n이고 a*b >= k인 조합을 찾는다
a = 0; b = 0
got_a_b = False
for _a in range(n):
    _b = n - _a
    if _a * _b >= k:
        a = _a
        b = _b
        got_a_b = True
        break
# print("a:", a, "b:", b)

if not got_a_b:
    print(-1)
    exit()

# 위에서 구한 a와 b를 이용해 쌍이 k개가 나오도록 만든다
# 먼저, 'B'를 b개 나열한다
result = 'B' * b

while a > 0:
    for i in range(len(result)):
        if k >= result[i:].count('B'):
            k -= result[i:].count('B')
            result = result[:i] + 'A' + result[i:]
            a -= 1
            break

print(result)