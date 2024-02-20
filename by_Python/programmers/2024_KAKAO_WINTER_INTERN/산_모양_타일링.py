def solution(n, tops):
    
    # dp[i] = i번째 삼각형까지 채우는 방법의 수
    dp = [0] * (2*n+2)
    dp[0] = 1
    
    for i in range(1, 2*n + 2):
        if i == 1:
            dp[i] = 1
            continue
            
        # 사다리꼴 윗변에 붙인 정삼각형이 있는지 확인
        if i % 2 == 0 and tops[i//2 - 1] == 1:
            dp[i] = (dp[i-1] * 2 + dp[i-2]) % 10007
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % 10007
    
    answer = dp[2*n+1]
    return answer

inputs = [(4, [1, 1, 0, 1]),
          (2, [0, 1]),
          (10, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])]
results = [149, 11, 7704]

for i in range(3):
    n, tops = inputs[i]
    print(solution(n, tops) == results[i])