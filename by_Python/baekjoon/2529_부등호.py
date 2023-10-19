import sys
input = sys.stdin.readline

k = int(input())
signs = input().split()

visited = [False] * 10
def solve(num, sign_idx, memo):
    if sign_idx == len(signs):
        # 성공
        results.append(memo)
        return

    sign = signs[sign_idx]
    if sign == '<':
        for next in range(num + 1, 10):
            if not visited[next]:
                visited[next] = True
                solve(next, sign_idx + 1, memo + str(next))
                visited[next] = False
        
    else:
        for next in range(0, num):
            if not visited[next]:
                visited[next] = True
                solve(next, sign_idx + 1, memo + str(next))
                visited[next] = False


results = []
for i in range(10):
    visited[i] = True
    solve(i, 0, str(i))
    visited[i] = False

# 최대 정수
print(results[-1]) 
# 최소 정수
print(results[0])