import sys
input = sys.stdin.readline

N = int(input().strip())
A = [0] + list(map(int, input().split()))

# dp[i] = 길이가 i인 증가하눈 부분 수열에서 마지막 숫자가 될 수 있는 최소값
# seq[i] = 길이가 i인 증가하는 부분 수열
seq = [[]]
for i in range(1, N+1):
    """
    print("i:", i)
    print("dp:", dp)
    print("sq:", seq)
    """
    if dp[-1] < A[i]:
        dp.append(A[i])
        seq.append(seq[-1] + [A[i]])
    else:
        if A[i] in dp:
            continue
        for j in range(1, len(dp)):
            # 처음으로 A[i] < dp[j]가 되는 곳에서 dp[j] = A[i]로 업데이트
            if A[i] < dp[j]:
                dp[j] = A[i]
                seq[j] = seq[j-1] + [A[i]]
                break

print(len(dp) - 1)
result = ""
for x in seq[-1]:
    result += str(x) + " "
print(result.strip())
