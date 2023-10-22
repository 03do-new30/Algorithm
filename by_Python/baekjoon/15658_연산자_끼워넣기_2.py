import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())
k = plus + minus + multiply + divide # 연산자의 총 개수

max_result = -10000000000
min_result = 10000000000

# idx = 현재 a의 인덱스
# result = 현재까지 만들어진 식의 결과
def solve(idx, result, plus, minus, multiply, divide):
    global max_result
    global min_result

    if idx == n-1:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    
    if plus > 0:
        solve(idx + 1, result + a[idx + 1], plus - 1, minus, multiply, divide)
    
    if minus > 0:
        solve(idx + 1, result - a[idx + 1], plus, minus - 1, multiply, divide)
    
    if multiply > 0:
        solve(idx + 1, result * a[idx + 1], plus, minus, multiply - 1, divide)
    
    if divide > 0:
        if result < 0:
            tmp = -(-result // a[idx + 1])
            solve(idx + 1, tmp, plus, minus, multiply, divide - 1)
        else:
            solve(idx + 1, result // a[idx + 1], plus, minus, multiply, divide - 1)

solve(0, a[0], plus, minus, multiply, divide)
print(max_result)
print(min_result)