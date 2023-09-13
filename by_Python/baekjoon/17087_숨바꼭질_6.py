import sys
input = sys.stdin.readline

n, s = map(int, input().split(' '))
a = list(map(int, input().split(' ')))

### 1 ###
# 수빈이의 위치를 기준으로 얼마나 떨어져 있는지 구한다
for i in range(len(a)):
    a[i] = s - a[i]
    if a[i] < 0:
        a[i] *= -1

### 2 ###
# 떨어져 있는 거리들의 최대공약수를 구한다
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

if len(a) == 1:
    print(a[0])
else:
    answer = a[0]
    for i in range(1, len(a)):
        answer = gcd(answer, a[i])
    print(answer)