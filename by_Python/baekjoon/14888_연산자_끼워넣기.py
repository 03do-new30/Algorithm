def solve(x, op, i):
    global max_ans, min_ans
    if i == N:
        min_ans = min(min_ans, x)
        max_ans = max(max_ans, x)
        return

    # +
    if op[0] > 0:
        op[0] -= 1
        solve(x + A[i], op, i+1)
        op[0] += 1
    # -
    if op[1] > 0:
        op[1] -= 1
        solve(x - A[i], op, i+1)
        op[1] += 1
    # *
    if op[2] > 0:
        op[2] -= 1
        solve(x * A[i], op, i+1)
        op[2] += 1
    # /
    if op[3] > 0:
        op[3] -= 1
        if x < 0:
            result = -(-x // A[i])
            solve(result, op, i+1)
        else:
            solve(x // A[i], op, i+1)
        op[3] += 1


N = int(input())
A = list(map(int, input().split()))
# 0: +, 1:-, 2:*, 3:/
op = list(map(int, input().split()))
max_ans = -1000000000
min_ans = 1000000000
solve(A[0], op, 1)
print(max_ans)
print(min_ans)
