import sys
input = sys.stdin.readline

n = int(input().strip())
a = [0] + list(map(int, input().split()))

# dp[x] = x번 인덱스까지의 가장 큰 부분수열의 합
# x번 인덱스까지의 가장 "작은" 부분수열의 합은 a[x]일 것! (길이가 1)
# dp[x] = a[x]로 초기화한다
dp = a[:]

for i in range(1, n+1):
    #print(i, "번 인덱스까지의 가장 큰 부분수열의 합 구하기")
    for j in range(1, i):
        if a[j] < a[i]:  # 증가하는 수열일 때
            #print(j, "번 인덱스 뒤에", i, "번 인덱스가 올 때 합은", dp[j] + a[i])
            dp[i] = max(dp[i], dp[j] + a[i])
    # print(dp)
    # print('-'*20)
print(max(dp))

# 반례
# 8
# 3 10 2 7 11 5 13 8
# 3 + 10 + 11 + 13 = 37이 되어야 함
