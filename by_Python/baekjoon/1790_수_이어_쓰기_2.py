import sys
input = sys.stdin.readline

n, k = map(int, input().split())

left = 1
right = n



# x까지 수를 이었을 때 총 수의 길이 계산
# 1 ~ 9 : 9
# 10 ~ 99 : 99 - 10 + 1 = 90 * 2 = 180
# 100 ~ 999 : 999 - 100 + 1 = 900 * 3 = 2700
def calc(x):
    ret = 0
    while x > 0:
        length = len(str(x))
        tmp = (x - 10**(length-1) + 1) * length
        ret += tmp
        x = (10 ** (length-1)) - 1
    return ret

if calc(n) < k:
    print(-1)
    exit()
    
while left <= right:
    mid = (left + right) // 2
    # print("left:", left, "mid:", mid, "right:", right)
    length = calc(mid)
    # print("length:", length)
    if length > k:
        right = mid-1
    elif length < k:
        left = mid + 1
    else:
        break

print(str(mid)[-1-abs(length - k)])
