def solution(alp, cop, problems):
    # 모든 문제를 풀 수 있게 하는 알고력과 코딩력을 구함
    alp_goal = max(x[0] for x in problems)
    cop_goal = max(x[1] for x in problems)

    # dp[i][j] = 알고력 i, 코딩력 j 상태에 도달하는 데 필요한 최단 시간
    dp = [[15000] * (cop_goal + 1) for _ in range(alp_goal + 1)]
    alp = min(alp, alp_goal)
    cop = min(cop, cop_goal)
    dp[alp][cop] = 0 # 초기상태 설정

    for i in range(alp, alp_goal + 1):
        for j in range(cop, cop_goal + 1):
            # 알고리즘 공부를 해서 (i+1, j) 상태로 만듦
            if i + 1 <= alp_goal:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            # 코딩 공부를 해서 (i, j+1) 상태가 된 경우
            if j + 1 <= cop_goal:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            # 문제를 풂
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    next_i = min(alp_goal, i + alp_rwd)
                    next_j = min(cop_goal, j + cop_rwd)
                    dp[next_i][next_j] = min(dp[next_i][next_j], dp[i][j] + cost)
    answer = dp[alp_goal][cop_goal]
    return answer
    

alp = [10, 0]
cop = [10, 0]
problems = [
    [[10,15,2,1,2],[20,20,3,3,4]],
    [[0,0,2,1,2],[4,5,3,1,2],[4,11,4,0,2],[10,4,0,4,2]]
]
result = [15, 13]

for i in range(len(result)):
    print(solution(alp[i], cop[i], problems[i]) == result[i])
    print('-' * 40)