import sys
from collections import deque
input = sys.stdin.readline


for testcase in range(int(input().strip())):
    """ 입력 """
    # N: 건물의 개수, K: 규칙의 개수
    N, K = map(int, input().split())

    # 건물 건설에 걸리는 시간
    D = [0] + list(map(int, input().split()))

    # rules: 건설 순서 인접 리스트
    # degree: 진입차수 저장
    rules = [[] for _ in range(N+1)]
    degree = [0]*(N+1)
    for _ in range(K):
        first, last = map(int, input().split())
        rules[first].append(last)
        degree[last] += 1

    # W: 건설해야 할 건물의 번호
    W = int(input().strip())
    """ 압력 끝 """

    # dp[i] = 건물 i를 건설하는 데 걸리는 최소 시간
    dp = [0]*(N+1)
    # 큐
    q = deque([])

    # 진입차수가 0인 것을 큐에 삽입
    for i in range(1, N+1):
        if degree[i] == 0:
            q.append(i)
            dp[i] = D[i]

    while q:
        i = q.popleft()
        for j in rules[i]:
            degree[j] -= 1  # 진입 차수를 줄인다
            dp[j] = max(dp[i] + D[j], dp[j])
            # 진입 차수가 0이 되면 큐에 삽입한다
            if degree[j] == 0:
                q.append(j)
    print(dp[W])
