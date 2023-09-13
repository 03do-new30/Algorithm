import sys
input = sys.stdin.readline

### 1 ###
cursor_left = [] # 커서를 기준으로 왼쪽
cursor_right = [] # 커서를 기준으로 오른쪽
string = input().strip()
for s in string:
    cursor_left.append(s)

m = int(input().strip())

for _ in range(m):
    cmd = input().strip()
    # print("커맨드:", cmd)
    if cmd[0] == 'L':
        if len(cursor_left) > 0:
            cursor_right.append(cursor_left.pop())
    elif cmd[0] == 'D':
        if len(cursor_right) > 0:
            cursor_left.append(cursor_right.pop())
    elif cmd[0] == 'B':
        if len(cursor_left) > 0:
            cursor_left.pop()
    else:
        add_char = cmd.split()[1]
        cursor_left.append(add_char)
    # print(cursor_left, "커서", cursor_right)

print(''.join(cursor_left) + ''.join(cursor_right[-1::-1]))