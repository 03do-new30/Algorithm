"""
단기간 성장
- 나머지 연산의 분배 법칙
- 페르마의 소정리
"""
N, K = map(int, input().split())
P = 1000000007
# nCk = (n!((n-k)!k!)^(p-2)) % p

# 나머지 연산을 적용한 팩토리얼 값 계산
def factorial(N):
    n = 1
    for i in range(2, N+1):
        n = (n*i) % P
    return n

# 나머지 연산을 적용한 거듭제곱 값 계산
def square(n, k):
    if k == 0:
        return 1
    elif k == 1:
        return n
    tmp = square(n, k // 2)
    if k % 2:
        return tmp * tmp * n % P
    else:
        return tmp * tmp % P

left = factorial(N)
right = factorial(N-K) * factorial(K) % P
print(left * square(right, P-2) % P)