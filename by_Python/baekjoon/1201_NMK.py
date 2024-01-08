import sys
input = sys.stdin.readline

"""
백준 강의 해설 참고하여 풂
"""

n, m, k = map(int, input().split())

if m + k - 1 <= n <= m * k:
    # 1-n까지 오름차순으로 정렬된 수
    # m개의 group으로 나눈 뒤, group별로 내림차순 정렬
    #   -> 각 group에서 랜덤 숫자 하나씩 뽑으면 LIS
    # 적어도 하나의 group은 k개의 수로 구성되어있어야 함 (최대 k개)
    #   -> 하나의 group 내 k개의 수 LDS
    arr = [x for x in range(1, n+1)]
    
    # 그룹의 경계 저장
    g = [0, k]
    n -= k # 0~k까지의 그룹이 만들어졌음
    m -= 1

    # 그룹 사이즈
    g_size = 1 if m == 0 else n // m
    remain = 0 if m == 0 else n % m

    for i in range(m):
        g += [g[-1] + g_size + (1 if remain > 0 else 0)]
        if remain > 0:
            remain -= 1
    
    for i in range(len(g) - 1):
        u = g[i]
        v = g[i + 1]
        arr[u:v] = arr[u:v][::-1] # 그룹 뒤집기
    
    print(' '.join(map(str, arr)))
else:
    print(-1)