import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
signs = list(map(int, input().split())) # +, -, *, //

min_result = 10000000000
max_result = -10000000000
def solve(idx, result):

    global min_result
    global max_result

    if idx == n-1:
        min_result = min(min_result, result)
        max_result = max(max_result, result)
        return
    
    for i in range(4):
        if signs[i] <= 0:
            continue
        if i == 0: # +
            signs[i] -= 1
            solve(idx + 1, result + a[idx+1])
            signs[i] += 1
        elif i == 1: # -
            signs[i] -= 1
            solve(idx + 1, result - a[idx+1])
            signs[i] += 1
        elif i == 2: # *
            signs[i] -= 1
            solve(idx + 1, result * a[idx+1])
            signs[i] += 1
        else: # //
            signs[i] -= 1
            # 음수를 양수로 나눌 때
            if result < 0 and a[idx + 1] > 0:
                tmp = -result // a[idx + 1]
                solve(idx + 1, -tmp)
            else:
                solve(idx + 1, result // a[idx+1])
            signs[i] += 1

solve(0, a[0])
print(max_result)
print(min_result)