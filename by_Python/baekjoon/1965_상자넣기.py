import sys
import bisect
input = sys.stdin.readline

n = int(input())
arr = [0] + list(map(int, input().split()))

# LIS = O(NlogN)
# dp[i] = 길이가 i인 증가하는 부분 수열의 마지막 숫자의 최소값
# 출처: https://seohyun0120.tistory.com/entry/%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4LIS-%EC%99%84%EC%A0%84-%EC%A0%95%EB%B3%B5-%EB%B0%B1%EC%A4%80-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# bisect.bisect_left(arr, x): arr이 정렬되어 있을 때, x가 들어갈 위치를 반환한다.


def LIS():
    dp = [0]
    for i in range(1, n+1):
        if arr[i] > dp[-1]:
            dp.append(arr[i])
        else:
            idx = bisect.bisect_left(dp, arr[i])  # 이분탐색으로 들어갈 자리 찾기
            dp[idx] = arr[i]
    return len(dp) - 1

# LIS - O(N^2)
# dp[i] = i상자를 포함하여, 넣을 수 있는 상자 개수


def solve():
    dp = [0] + [1]*n  # 초기 dp[i] = 1 (자기자신의 개수)
    for i in range(1, n+1):
        # i보다 앞 순서 상자들을 체크하며
        # arr[i]보다 크기가 작은 것들 중 상자 개수가 max인 것을 고름
        max_box = 0
        for j in range(i):
            if arr[j] < arr[i]:
                max_box = max(max_box, dp[j])
        dp[i] += max_box

    return max(dp)


ans = LIS()
print(ans)
