import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
signs = list(map(int, input().split())) # +, -, *, //

min_result = 10000000000
max_result = -10000000000

def solve(count, result):
    global min_result
    global max_result

    # 연산자를 모두 다 쓰면 중단
    if count == n-1:
        min_result = min(min_result, result)
        max_result = max(max_result, result)
        return
    
    for i in range(4):
        if signs[i] > 0:
            signs[i] -= 1
            if i == 0: # +
                solve(count + 1, result + a[count + 1])
            elif i == 1: # -
                solve(count + 1, result - a[count + 1])
            elif i == 2: # *
                solve(count + 1, result * a[count + 1])
            elif i == 3: # //
                if result < 0:
                    tmp = -(-result // a[count + 1])
                    solve(count + 1, tmp)
                else:
                    solve(count + 1, result // a[count + 1])
            signs[i] += 1

solve(0, a[0])
print(max_result)
print(min_result)