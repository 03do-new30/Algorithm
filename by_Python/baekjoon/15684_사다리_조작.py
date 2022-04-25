# 출처: https://ryu-e.tistory.com/69
import sys
input = sys.stdin.readline

# i번 세로선의 결과가 i번이 나오는지 체크하는 함수
def check():
    for dest in range(1, N+1):
        col = dest
        for row in range(1, H+1):
            if arr[row][col]:
                col += 1
            elif 0 <= col-1 and arr[row][col-1]:
                col -= 1
        
        if col != dest:
            return False
    return True


def dfs(cnt, r, c):
    global ans
    
    if check():
        ans = min(ans, cnt)
        return
    
    # cnt가 3이면 다음에는 4를 검사해야하므로 중단
    # ans < cnt이면 최소값이 아니므로 중단
    if cnt == 3 or ans < cnt:
        return
    
    for i in range(r, H+1):
        # 가로선을 우선적으로 탐색한다
        if i == r:
            # 행이 변경되기 전에는 c열에서부터 탐색
            k = c
        else:
            # 행이 변경될 경우 1열에서부터 탐색
            k = 1
        
        for j in range(k, N):
            if not arr[i][j]:
                # 가로선을 긋고, 연속된 가로선을 긋지 않기 위해 j + 2를 호출한다
                arr[i][j] = True
                dfs(cnt + 1, i, j+2) # cnt 1 증가, 세로선은 그대로, 연속해서 두 사다리가 오면 안되므로 가로선은 2 증가
                arr[i][j] = False



# main
N, M, H = map(int, input().split())
arr = [[False]*(N+1) for _ in range(H+1)]

# 가로선 입력
for _ in range(M):
    a, b = map(int, input().split())
    arr[a][b] = True

ans = 4
dfs(0, 1, 1)
if ans <= 3:
    print(ans)
else:
    print(-1)