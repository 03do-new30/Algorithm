from collections import deque
def solution(rc, operations):
    n = len(rc); m = len(rc[0])
    
    rows = deque(deque(rc_row[1:m-1]) for rc_row in rc)
    left_cols = deque(rc_row[0] for rc_row in rc)
    right_cols = deque(rc_row[m-1] for rc_row in rc)
    
    for operation in operations:
        if operation == "ShiftRow":
            rows.rotate()
            left_cols.rotate()
            right_cols.rotate()
        else: # Rotate
            rows[0].appendleft(left_cols.popleft())
            right_cols.appendleft(rows[0].pop())
            rows[-1].append(right_cols.pop())
            left_cols.append(rows[-1].popleft())
    
    answer = []
    for r in range(n):
        answer.append([left_cols[r]] + list(rows[r]) + [right_cols[r]])
        
    return answer

rc = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[8, 6, 3], [3, 3, 7], [8, 4, 9]],
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
]
operations = [[
    "Rotate", "ShiftRow"], 
    ["Rotate", "ShiftRow", "ShiftRow"],
    ["ShiftRow", "Rotate", "ShiftRow", "Rotate"]]
result = [
    [[8, 9, 6], [4, 1, 2], [7, 5, 3]],
    [[8, 3, 3], [4, 9, 7], [3, 8, 6]],
    [[1, 6, 7 ,8], [5, 9, 10, 4], [2, 3, 12, 11]]
]

for i in range(len(result)):
    print("#", i+1, solution(rc[i], operations[i]) == result[i])
    print('-' * 40)