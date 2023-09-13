import sys
input = sys.stdin.readline


def gcd(a, b):
    if b == 0:
        return a
    r = a % b
    return gcd(b, r)

t = int(input())
for _ in range(t):
    nums = list(map(int, input().split(' ')))[1:]
    answer = 0
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            answer += gcd(nums[i], nums[j])
    print(answer)