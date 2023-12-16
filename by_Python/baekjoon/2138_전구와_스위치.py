import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, list(input().strip())))
goal = list(map(int, list(input().strip())))

def switch(a, idx):
    for i in range(idx-1, idx+2):
        if 0 <= i < n:
            a[i] = (a[i] + 1) % 2

def solve(on):
    cur = arr[:]
    cnt = 0 # 버튼을 누른 횟수
    
    if on: # 0번째 버튼을 누른 경우
        cnt += 1
        switch(cur, 0)
    
    for i in range(1, n):
        # print("i:", i, end=' ')
        if cur[i-1] != goal[i-1]:
            # print("스위치")
            switch(cur, i)
            cnt += 1
            # print("-> cur:", cur)
        # else:
        #     print("스킵")
    
    for i in range(n):
        if cur[i] != goal[i]:
            return (False, -1)
    return (True, cnt)
    

# 0번째 버튼을 누르지 않은 경우 (on = False)
off_result, off_cnt = solve(False)
# 0번째 버튼을 누른 경우 (on = True)
on_result, on_cnt = solve(True)

if off_result and on_result:
    print(min(off_cnt, on_cnt))
elif off_result and not on_result:
    print(off_cnt)
elif not off_result and on_result:
    print(on_cnt)
else:
    print(-1)
