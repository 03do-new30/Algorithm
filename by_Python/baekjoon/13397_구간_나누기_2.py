import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 구간의 점수를 mid로 만든다고 했을 때, 몇등분 나오는가
left  = 0
right = max(arr)
ans = right

def go(mid):
    t1 = arr[0] # 구간에서 가장 작은 값
    t2 = arr[0] # 구간에서 가장 큰 값
    ans = 1
    for i in range(1, n):
        if t1 > arr[i]:
            t1 = arr[i]
        if t2 < arr[i]:
            t2 = arr[i]
        if t2 - t1 > mid: # 구간이 하나 만들어진다
            ans += 1
            t1 = arr[i]
            t2 = arr[i]
    # print("mid:", mid, "ans:", ans)
    return ans # 구간의 개수

# mid보다 큰 구간이 있는지 확인해준다
while left <= right:
    mid = (left + right) // 2
    if go(mid) <= m:
        # m개 구간 이하로 나누어서
        # 구간 점수의 최대값을 mid로 맞출 수 있을 때
        # 구간 점수의 최대값을 줄여본다
        right = mid - 1
        if ans > mid:
            ans = mid
    else:
        left = mid + 1
print(ans)