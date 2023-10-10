import sys
input = sys.stdin.readline

n, s = map(int, input().split())
nums = list(map(int, input().split()))

# 비트마스킹을 이용해 부분집합 구하기
# arr[i] = 부분집합 i의 합을 저장
arr = [0] * (1 << n)

for i in range(len(arr)):
    total = 0 # 합 저장
    
    # j번째 수가 부분집합 i에 포함되는지 확인한다
    for j in range(n):
        if i & (1 << j) > 0: #포함
            total += nums[j]
    
    arr[i] = total

# 공집합(0)인 경우를 제외하고, 합이 S가 되는 경우를 센다
answer = 0
for i in range(1, len(arr)):
    if arr[i] == s:
        answer += 1

print(answer)