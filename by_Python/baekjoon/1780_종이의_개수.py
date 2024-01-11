import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

count = {-1:0, 0:0, 1:0}

# (r, c) -> 종이의 가장 왼쪽 상단 좌표
# edge_size -> 한 변의 길이
def solve(r, c, edge_size):
    # 같은 수로 되어 있는지 확인한다
    perfect = True
    for i in range(r, r + edge_size):
        for j in range(c, c + edge_size):
            if arr[r][c] != arr[i][j]:
                perfect = False
                break
    
    if perfect:
        count[arr[r][c]] += 1
        return
    else:
        # 종이를 같은 크기의 종이 9개로 자른다
        new_edge = edge_size // 3
        solve(r, c, new_edge)
        solve(r + new_edge, c, new_edge)
        solve(r + new_edge * 2, c, new_edge)

        solve(r, c + new_edge, new_edge)
        solve(r + new_edge, c + new_edge, new_edge)
        solve(r + new_edge * 2, c + new_edge, new_edge)

        solve(r, c + new_edge * 2, new_edge)
        solve(r + new_edge, c + new_edge * 2, new_edge)
        solve(r + new_edge * 2, c + new_edge * 2, new_edge)

solve(0, 0, n)
print(count[-1])
print(count[0])
print(count[1])