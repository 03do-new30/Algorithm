import sys
input = sys.stdin.readline

m = int(input())
s = 0

for _ in range(m):
    cmd = input().split()

    if cmd[0] == "add":
        x = int(cmd[1]) -1
        s = s | (1 << x)
    elif cmd[0] == "remove":
        x = int(cmd[1]) -1
        s = s & ~(1 << x)
    elif cmd[0] == "check":
        x = int(cmd[1]) -1
        if s & (1 << x) > 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == "toggle":
        x = int(cmd[1]) -1
        s = s ^ (1 << x)
    elif cmd[0] == "all":
        s = (1 << 20) - 1
    else:
        s = 0
