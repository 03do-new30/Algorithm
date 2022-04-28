import sys
input = sys.stdin.readline

def is_zero(arr):
    for row in arr:
        for x in row:
            if x != 0:
                return False
    return True

def is_one(arr):
    for row in arr:
        for x in row:
            if x != 1:
                return False
    return True

def solve(arr, _len):
    global answer
    
    if is_zero(arr):
        answer += "0"
    elif is_one(arr):
        answer += "1"
    else:
        quad_1 = []
        quad_2 = []
        for r in range(_len//2):
            quad_1.append(arr[r][:_len//2])
            quad_2.append(arr[r][_len//2:])
        quad_3 = []
        quad_4 = []
        for r in range(_len//2, _len):
            quad_3.append(arr[r][:_len//2])
            quad_4.append(arr[r][_len//2:])
        answer += "("
        solve(quad_1, _len//2)
        solve(quad_2, _len//2)
        solve(quad_3, _len//2)
        solve(quad_4, _len//2)
        answer += ")"

N = int(input())
arr = [list(map(int, list(input().strip()))) for _ in range(N)]

answer = ""
solve(arr, N)
print(answer)