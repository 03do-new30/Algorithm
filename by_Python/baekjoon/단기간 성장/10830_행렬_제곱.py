n, b = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# 행렬 x와 y의 곱셈 결과를 반환한다
def matrix_mul(x, y):
    result = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            tmp = 0
            for i in range(n):
                tmp += x[r][i] * y[i][c]
            result[r][c] = tmp % 1000
    return result

# 분할정복
def divide_and_conquer(a, b):
    if b == 1:
        result = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                result[r][c] = a[r][c] % 1000
        return result
    tmp = divide_and_conquer(a, b//2)
    # b가 짝수인 경우
    if b % 2 == 0:
        return matrix_mul(tmp, tmp)
    else: # 홀수
        return matrix_mul(a, matrix_mul(tmp, tmp))

result = divide_and_conquer(a, b)
for r in range(n):
    print(' '.join(map(str, result[r])))