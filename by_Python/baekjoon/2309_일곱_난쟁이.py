import sys
input = sys.stdin.readline

nums = []
for _ in range(9):
    nums.append(int(input()))

nums.sort()
all_sum = sum(nums)

for i in range(8):
    for j in range(i+1, 9):
        if all_sum - nums[i] - nums[j] == 100:
            for idx in range(9):
                if idx == i:
                    continue
                if idx == j:
                    continue
                print(nums[idx])
            exit()