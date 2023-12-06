import sys
input = sys.stdin.readline
from collections import deque

# 소수 판별 - 에라토스테네스의 체
primes = [True] * (10000)
for i in range(2, 10000):
    if primes[i]:
        for j in range(i + i, 10000, i):
            primes[j] = False

t = int(input())
for _ in range(t):
    a, goal = map(int, input().split())
    visited = [False] * 10000
    q = deque([(a, 0)])
    visited[a] = True

    result = -1

    while q:
        a, cnt = q.popleft()
        if a == goal:
            result = cnt
            break
        str_a = str(a)
        # 각 자리수를 바꾸어가며 테스트
        for i in range(4):
            for j in range(10): # 0-9
                new_a = int(str_a[:i] + str(j) + str_a[i+1:])
                if 1000 <= new_a < 10000:
                    if primes[new_a] and not visited[new_a]:
                        visited[new_a] = True
                        q.append((new_a, cnt + 1))
    
    if result == -1:
        print("Impossible")
    else:
        print(result)