import sys
input = sys.stdin.readline

t = int(input())
nums = []
for _ in range(t):
    nums.append(int(input()))
max_num = max(nums)

# 에라토스테네스의 체
erased = [False for i in range(1000001)]

for i in range(2, max_num + 1):
    if not erased[i]:
        for j in range(i + i, max_num + 1, i):
            erased[j] = True

# 골드바흐 파티션 판정
for num in nums:
    answer = 0
    for i in range(2, num // 2 + 1):
        if not erased[i] and not erased[num - i] and i <= num-i:
            answer += 1
    print(answer)