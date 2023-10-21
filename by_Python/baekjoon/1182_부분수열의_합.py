import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0

# idx -> 부분수열에 포함해야할지 말지 결정해야하는 인덱스
# sum -> 현재까지 부분수열의 합
def solve(idx, sum):
    global answer
    
    if idx == n and sum == s:
        answer += 1
        return
    
    if idx == n and sum != s:
        return
    
    # idx번째 수를 선택하는 경우
    solve(idx + 1, sum + nums[idx])
    # idx번째 수를 선택하지 않는 경우
    solve(idx + 1, sum)

solve(0, 0)
if s == 0:
    # 공집합 제거해주기
    answer -= 1
print(answer)