import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))

# 부분수열의 합을 다 구한 뒤, 중복 제거하고 오름차순으로 정렬해본다
results = set()
def solve(idx, result):
    if idx == n:
        results.add(result)
        return

    if idx > n:
        return
    
    # idx번째 수를 고르는 경우
    solve(idx + 1, result + s[idx])
    # idx번째 수를 고르지 않는 경우
    solve(idx + 1, result)

solve(0, 0)
results = list(results)
results.sort()

idx = 0
for number in range(2000001):
    if idx >= len(results):
        print(number)
        break

    if results[idx] != number:
        print(number)
        break
    
    idx += 1