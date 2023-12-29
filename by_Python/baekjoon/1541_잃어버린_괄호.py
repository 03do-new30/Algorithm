import sys
input = sys.stdin.readline

initial = input().strip()
signs = []
for i in range(len(initial)):
    if initial[i] in ('+', '-'):
        signs.append(initial[i])
        initial = initial[:i] + ' ' + initial[i+1:]
nums = list(map(int, initial.split())) # 숫자

# '-'가 나오면 항상 뒤의 식을 모두 '-'로 만들 수 있다
minus = False
ans = 0
for i in range(len(nums)):
    if not minus:
        ans += nums[i]
        if i < len(signs) and signs[i] == '-':
            minus = True
    else:
        ans -= nums[i]

print(ans)