def solution(board, skill):
    n = len(board); m =len(board[0])
    # 누적합을 이용한다
    # 누적합이 만들어질 수 있도록 새로운 배열을 만든다
    # 2차원 배열에서 (x1, y1) ~ (x2, y2)까지 n만큼 변화는
    # (x1, y1)에 +n (x1, y2)에 -n
    # (x2, y1)에 -n (x2, y2)에 +n
    tmp = [[0] * m for _ in range(n)]
    for type, r1, c1, r2, c2, degree in skill:
        if type == 1: # 공격
            degree = -degree
        tmp[r1][c1] += degree
        if c2 + 1 < m:
            tmp[r1][c2 + 1] -= degree
        if r2 + 1 < n:
            tmp[r2 + 1][c1] -= degree
        if r2 + 1 < n and c2 + 1 < m:
            tmp[r2 + 1][c2 + 1] += degree
    # 각 원소에 더해질 내구도를 누적합을 통해 O(nm)만에 구할 수 있다
    # 1. 위에서 아래로 누적합
    for c in range(m):
        for r in range(n):
            if r == 0:
                continue
            else:
                tmp[r][c] = tmp[r-1][c] + tmp[r][c]
    # 2. 왼쪽에서 오른쪽으로 누적합
    for r in range(n):
        for c in range(m):
            if c == 0:
                continue
            else:
                tmp[r][c] = tmp[r][c-1] + tmp[r][c]
    
    # 누적합 배열과 board 배열을 합쳐주면서
    # 0보다 큰 정수의 개수를 구한다
    answer = 0
    for r in range(n):
        for c in range(m):
            if board[r][c] + tmp[r][c] > 0:
                answer += 1
    return answer

board = [
    [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],
    [[1,2,3],[4,5,6],[7,8,9]]	
]
skill = [
	[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]],
    [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]	
]
result = [10, 6]

for i in range(len(result)):
    print(solution(board[i], skill[i]) == result[i])
    print('-' * 30)