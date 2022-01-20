import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int, input().split()))


def LIS(part_of_a, k):
    # dp[x] = 길이가 x를 만족하는 수열들 중, 마지막 숫자의 최소값
    dp = [0]

    for i in range(len(part_of_a)):
        # k (Sk를 나타냄)보다 크거나 같으면, 증가부에 들어갈 수 없음
        if part_of_a[i] >= k:
            continue

        if dp[-1] < part_of_a[i]:
            dp.append(part_of_a[i])

        else:
            # 이미 존재하는 값이면 스킵
            if part_of_a[i] in dp:
                continue
            # 들어갈 수 있는 자리 찾기
            for j in range(len(dp)):
                if dp[j] > part_of_a[i]:
                    dp[j] = part_of_a[i]
                    break
    return len(dp) - 1


# 수열 a의 각 숫자가 각각 Sk일 때, 그 중 가장 긴 것 찾기
max_len = 0
for k in range(n):

    # Sk를 포함하지 않은 좌측 (증가부)
    left = a[:k]
    # Sk를 포함하지 않은 우측 (감소부)
    right = a[k+1:]

    # 증가부의 길이
    left_len = LIS(left, a[k])

    # 감소부의 길이
    # right를 reverse해줘야 함!
    right.reverse()
    right_len = LIS(right, a[k])

    # Sk는 무조건 수열에 들어가 있어야 하므로,
    # 증가부 길이 + 감소부 길이 + 1 (Sk)
    total_len = left_len + right_len + 1
    max_len = max(max_len, total_len)

print(max_len)
