import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 0과 1로 바꾸면 비트마스크로도 해결 가능하다
# idx번째 사람을 어떤 팀에 넣을지 결정한다
def solve(idx, team_a, team_b):
    if idx == n:
        if len(team_a) != n // 2:
            return -1
        if len(team_b) != n // 2:
            return -1
        
        stat_a = 0
        stat_b = 0
        
        for i in range(n // 2 - 1):
            for j in range(i, n // 2):
                stat_a += arr[team_a[i]][team_a[j]] + arr[team_a[j]][team_a[i]]
                stat_b += arr[team_b[i]][team_b[j]] + arr[team_b[j]][team_b[i]]
        
        diff = abs(stat_a - stat_b)
        return diff
    
    answer = -1
    
    # a팀
    tmp = solve(idx + 1, team_a + [idx], team_b)
    if tmp != -1:
        answer = tmp
    # b팀
    tmp = solve(idx + 1, team_a, team_b + [idx])
    if tmp != -1:
        if answer != -1:
            answer = min(answer ,tmp)
        else:
            answer = tmp
    
    return answer

print(solve(0, [], []))
