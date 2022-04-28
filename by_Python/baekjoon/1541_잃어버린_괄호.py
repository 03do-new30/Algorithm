import sys
input = sys.stdin.readline

# - 뒤에 나오는 값들은 합쳐서 뺴주면 된다
in_ = input().split('-')
nums = []
for x in in_:
    x = x.split('+')
    tmp = 0
    for num in x:
        tmp += int(num)
    nums.append(tmp)

# 첫번째 num은 더해주고, 나머지는 빼주면 됨
ans = 0
first = True
for num in nums:
    if first:
        ans += num
        first = False
    else:
        ans -= num

print(ans)
