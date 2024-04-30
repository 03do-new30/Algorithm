from collections import deque

def solution(rows, columns, queries):
    answer = []
    # 행렬
    n = rows; m = columns
    arr = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            arr[r][c] = r * m + (c + 1)
    for query in queries:
        r1, c1, r2, c2 = query
        r1 -= 1; c1 -= 1; r2 -= 1; c2 -= 1
        numbers = deque()
        # 테두리에 있는 숫자들을 numbers에 담는다
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        nr = r1; nc = c1
        for i in range(4):
            while r1 <= nr + dr[i] <= r2 and c1 <= nc + dc[i] <= c2:
                numbers.append(arr[nr][nc])
                nr += dr[i]
                nc += dc[i]
        # 회전하는 숫자 중 가장 작은 숫자를 배열에 담는다
        answer.append(min(numbers))
        # numbers를 회전한다
        numbers.rotate()
        # 숫자들을 차례로 행렬에 넣는다
        nr = r1; nc = c1
        for i in range(4):
            while r1 <= nr + dr[i] <= r2 and c1 <= nc + dc[i] <= c2:
                arr[nr][nc] = (numbers.popleft())
                nr += dr[i]
                nc += dc[i]
    return answer

rows = [6, 3, 100]
columns = [6, 3, 97]
queries= [[[2,2,5,4],[3,3,6,6],[5,1,6,3]]	,
          [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]	,
          [[1,1,100,97]]]
result = [[8, 10, 25],
          [1, 1, 5, 3],
          [1]]

for i in range(len(result)):
    print(result[i] == solution(rows[i], columns[i], queries[i]))