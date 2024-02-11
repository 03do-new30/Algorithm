import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [*map(int, input().split())]

if n <= m:
    print(n)
    exit()

# 몇분째(시간)에 모든 아이를 다 태우는지를 기준으로 이분탐색
left = 0
right = 2000000000 * 1000000
all_boarded = right

while left <= right:
    # mid분째에 몇번째 아이가 타는지
    mid = (left + right) // 2

    # mid분째까지 탄 사람 수
    cnt = m
    for num in arr:
        cnt += mid // num
    
    # mid분째까지 탄 사람 수가 마지막 아이의 번호보다 작다면
    if cnt < n:
        # 범위를 늘려본다
        left = mid + 1
    else:
        right = mid - 1
        all_boarded = min(all_boarded, mid) # 아이들을 다 태우는 최소 시간

# 아이들을 다 태우는 최소 시간을 구했다면,
# 몇번째 놀이기구에 마지막 아이가 타는지 구해야 한다

# (all_boarded - 1)분째에는 몇명이 타는가?
tmp_cnt = m
for num in arr:
    tmp_cnt += (all_boarded - 1) // num

# (all_boarded - 1)분째부터 시작해서 몇번째 놀이기구에 마지막 사람이 들어가는지 확인한다
answer = 0
for i in range(m):
    if all_boarded % arr[i] == 0:
        tmp_cnt += 1
        # 지금 탄 놀이기구까지 해서 tmp_cnt == m이 되는가?
        if tmp_cnt == n:
            answer = i
            break

print(answer + 1) # 인덱스 -> x번째로 변환해준다