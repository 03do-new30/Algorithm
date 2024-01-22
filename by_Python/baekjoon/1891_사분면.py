import sys
input = sys.stdin.readline

d, num = map(int, input().split())
col_move, row_move = map(int, input().split())

# 한자리수 - 전체 2*2
# 두자리수 사분면 - 전체 4*4
# 세자리수 사분면 - 전체 8*8

# num 글자의 위치를 찾는다
# 가장 왼쪽 위 좌표가 (r, c)이며 한 변의 길이는 edge
def get_xy(num, r, c, edge):
    if len(str(num)) == 1:
        if num == 1:
            return (r, c+1)
        elif num == 2:
            return (r, c)
        elif num == 3:
            return (r+1, c)
        else:
            return (r+1, c+1)
    
    current_quad = str(num)[0]
    next_quad = str(num)[1:]
    # 1사분면
    if current_quad == '1':
        return get_xy(int(next_quad), r, c + edge // 2, edge // 2)
    # 2사분면
    elif current_quad == '2':
        return get_xy(int(next_quad), r, c, edge // 2)
    # 3사분면
    elif current_quad == '3':
        return get_xy(int(next_quad), r + edge // 2, c, edge // 2)
    # 4사분면
    else:
        return get_xy(int(next_quad), r + edge // 2, c + edge // 2, edge // 2)

# 좌표로 사분면 번호를 구한다
# 가장 왼쪽 위 좌표가 (r, c)
def get_num(r, c, edge, tmp, x, y):
    if edge == 1:
        return int(tmp)

    if x < r + edge // 2:
        # 2사분면
        if y < c + edge // 2:
            tmp += '2'
            return get_num(r, c, edge // 2, tmp, x, y)
        # 1사분면
        else:
            tmp += '1'
            return get_num(r, c + edge // 2, edge // 2, tmp, x, y)
    else:
        # 3사분면
        if y < c + edge // 2:
            tmp += '3'
            return get_num(r + edge // 2, c, edge // 2, tmp, x, y)
        # 4사분면
        else:
            tmp += '4'
            return get_num(r + edge // 2, c + edge // 2, edge // 2, tmp, x, y)
    
    

x, y = get_xy(num, 0, 0, 2**d)

if 0 <= x - row_move < 2 ** d and 0 <= y + col_move < 2 ** d:
    new_x = x - row_move
    new_y = y + col_move
    new_num = get_num(0, 0, 2 ** d, "", new_x, new_y)
    print(new_num)
else:
    print(-1)