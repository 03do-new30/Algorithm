import sys
input = sys.stdin.readline

n = int(input())

t = [0 for _ in range(n+1)]
p = [0 for _ in range(n+1)]

for i in range(1, n+1):
    _t, _p = map(int, input().split())
    t[i] = _t
    p[i] = _p

answers = []
def solve(day, sum):
    if day == n + 1:
        answers.append(sum)
        return

    if day > n + 1:
        return
    
    solve(day + t[day], sum + p[day])
    solve(day + 1, sum)

solve(1, 0)
print(max(answers))