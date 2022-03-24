# LIS
"""
https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4
"""

import sys
import bisect
input = sys.stdin.readline

n = int(input().strip())
a = [0] + list(map(int, input().split()))

# O(N^2) 알고리즘


def LIS_1():
    # d[i] = a[i]를 마지막 값으로 가지는 LIS의 길이
    d = [0] + [0 for _ in range(n)]

    for i in range(1, n+1):
        can_add_after = []
        for j in range(0, i):
            # a[i]가 a[j]보다 크다면 그 뒤에 추가 가능
            if a[j] < a[i]:
                can_add_after.append(d[j])
        d[i] = max(can_add_after) + 1

    return max(d)


# O(NlogN) 알고리즘
# 만약 d[j] = k를 만족하는 j 중 a[i]의 값이 가장 작은 j만 저장해 놓으면
# 나중에 d[i] (i > j)를 계산할 때 그 값만 참조하면 d[i]의 값을 쉽게 알 수 있음
def LIS_2():
    # mini[k] = d[x]가 k를 만족하는 x들 중 최소값
    mini = [0]
    for i in range(1, n+1):
        if mini[len(mini)-1] < a[i]:
            mini.append(a[i])
        else:
            # 이분 탐색(logN)을 통해 들어갈 수 있는 인덱스를 찾는다
            # mini가 정렬되어있으므로 사용 가능
            idx = bisect.bisect_left(mini, a[i])
            mini[idx] = a[i]
            """
            # 이미 존재하는 값이면 스킵
            if a[i] in mini:
                continue
            # 아니면 들어갈 수 있는 자리 찾기
            for j in range(len(mini)):
                if mini[j] > a[i]:
                    mini[j] = a[i]
                    break
            """

    return len(mini) - 1


# print(LIS_1())
print(LIS_2())
