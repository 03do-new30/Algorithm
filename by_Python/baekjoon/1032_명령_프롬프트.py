import sys
input = sys.stdin.readline

N = int(input())
first = True
for _ in range(N):
    if first:
        cmd = list(input().strip())
        first = False
    else:
        current = input().strip()
        for i in range(len(cmd)):
            if cmd[i] == '?' or cmd[i] == current[i]:
                continue
            cmd[i] = '?'
print(''.join(cmd))