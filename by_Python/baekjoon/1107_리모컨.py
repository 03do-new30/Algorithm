import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

btns = [] # 고장나지 않은 버튼 저장
if m > 0:
    broken = list(map(int, input().split()))
    for i in range(10):
        if i not in broken:
            btns.append(i)
else:
    btns = [i for i in range(10)]

chnl = 100
cnt = 0
ans = 0

### 1 ###
# (+), (-)만으로 이동하는 경우 입력 횟수
plus_minus = abs(n - chnl)
ans = plus_minus

if ans == 0:
    print(ans)
    exit()

### 2 ###
# 입력한 채널에 고장난 번호가 포함되어 있는지 체크
def is_valid(channel):
    channel = str(channel)
    for number in channel:
        if int(number) not in btns:
            return False
    return True

### 3 ###
# 채널을 입력하는 경우
for i in range(1000001):
    # 고장난 버튼이 포함되어 있으면 안됨
    if is_valid(i):
        # 버튼으로 입력한 채널에서 (+) 혹은 (-)로 이동하는 입력 횟수
        tmp_ans = len(str(i)) + abs(i - n)
        # 작은 값을 저장
        ans = min(ans, tmp_ans)

print(ans)